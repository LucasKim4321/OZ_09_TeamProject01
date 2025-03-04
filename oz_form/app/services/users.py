from flask import Blueprint, request, redirect, flash, url_for
from app.models import db, User, AgeStatus, GenderStatus

users_bp = Blueprint('users', __name__)

@users_bp.route('/users/signup', methods=['POST'])
def signup_post():
    """회원가입 처리"""
    name = request.form.get('name')
    email = request.form.get('email')
    gender = request.form.get('gender')
    age = request.form.get('age')

    if not name or not email or not gender or not age:
        flash("모든 항목을 입력해야 합니다.", "danger")
        return redirect(url_for('routes.signup'))

    try:
        age_enum = AgeStatus[age]
        gender_enum = GenderStatus[gender]
    except KeyError:
        flash("잘못된 입력값입니다.", "danger")
        return redirect(url_for('routes.signup'))

    if get_user(email):
        flash("이미 가입된 이메일입니다.", "danger")
        return redirect(url_for('routes.signup'))

    user = User(name=name, email=email, gender=gender_enum, age=age_enum)

    try:
        db.session.add(user)
        db.session.commit()
        flash("회원가입이 완료되었습니다!", "success")
        return redirect(url_for('routes.question', question_id=1))
    except Exception as e:
        db.session.rollback()
        flash(f"회원가입 중 오류 발생: {str(e)}", "danger")
        return redirect(url_for('routes.signup'))

def get_user(email):
    """이메일로 사용자 조회"""
    return User.query.filter_by(email=email).first()
