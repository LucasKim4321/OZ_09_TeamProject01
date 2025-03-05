from flask import Blueprint, jsonify, request
from app.models import db, User

users_bp = Blueprint('users', __name__)

@users_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()

    # 필수 필드 추출
    name = data.get("name")
    email = data.get("email")
    age = data.get("age")
    gender = data.get("gender")

    # 유효성 검사 (age가 None인 경우 체크)
    if not name or not email or age is None or not gender:
        return jsonify({"error": "필수 입력값이 누락되었습니다."}), 400

    # 이메일 중복 확인
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify({"message": "이미 존재하는 계정 입니다."}), 409
    
        
    # 사용자 생성
    new_user = User(name=name, email=email, age=age, gender=gender)
    
    # 데이터베이스 저장
    db.session.add(new_user)
    db.session.commit()

    return jsonify({
        "message": f"{name}님 회원가입을 축하합니다.",
        "user_id": new_user.id,
        "age_group": age_group
    }), 200
