from flask import Blueprint, jsonify, request, render_template, redirect, flash, url_for
from app.models import db, User, AgeStatus, GenderStatus

routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    return render_template('index.html')

@routes.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        gender = request.form['gender']
        age = request.form['age']

        # Enum 타입으로 변환
        try:
            age_enum = AgeStatus[age]  # 문자열을 Enum으로 변환
            gender_enum = GenderStatus[gender]
        except KeyError:
            flash("잘못된 입력값입니다.", "danger")
            return redirect(url_for('routes.signup'))

        # 이미 존재하는 이메일 체크
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash("이미 가입된 이메일입니다.", "danger")
            return redirect(url_for('routes.signup'))

        # 새로운 사용자 생성
        new_user = User(name=name, email=email, gender=gender_enum, age=age_enum)

        # 데이터베이스에 저장
        try:
            db.session.add(new_user)
            db.session.commit()
            flash("회원가입이 완료되었습니다!", "success")

            # 회원가입 완료 후 /question/1 페이지로 리디렉션
            return redirect(url_for('routes.question', question_id=1))  
        except Exception as e:
            db.session.rollback()
            flash(f"회원가입 중 오류가 발생했습니다: {str(e)}", "danger")
            return redirect(url_for('routes.signup'))

    return render_template('signup.html')

@routes.route('/question/<int:question_id>')
def question(question_id):
    return render_template('question.html', question_id=question_id)

@routes.route('/result')
def result():
    return render_template('result.html')
