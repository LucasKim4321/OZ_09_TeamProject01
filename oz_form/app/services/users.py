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
    


    # 유효한 연령대 문자열 집합
    valid_age_groups = {"teen", "twenty", "thirty", "forty", "fifty"}
    age_group = None
    numeric_age = None

    
      # age_input이 숫자(int) 또는 숫자 문자열일 경우 처리
    if isinstance(age, int):
        numeric_age = age
    elif isinstance(age, str):
        if age.isdigit():
            numeric_age = int(age)
        elif age.lower() in valid_age_groups:
            # 프론트에서 이미 연령대 문자열("twenty" 등)으로 보낸 경우
            age_group = age.lower()
        else:
            return jsonify({"error": "나이 데이터 형식이 올바르지 않습니다."}), 400
    else:
        return jsonify({"error": "나이 데이터 형식이 올바르지 않습니다."}), 400

    # 숫자 형태의 나이가 있을 경우, 연령대 결정
    if numeric_age is not None:
        if 0 <= numeric_age < 20:
            age_group = "teen"
        elif 20 <= numeric_age < 30:
            age_group = "twenty"
        elif 30 <= numeric_age < 40:
            age_group = "thirty"
        elif 40 <= numeric_age < 50:
            age_group = "forty"
        else:
            age_group = "fifty"
        
    # 사용자 생성
    new_user = User(name=name, email=email, age=age_group, gender=gender)
    
    # 데이터베이스 저장
    db.session.add(new_user)
    db.session.commit()

    return jsonify({
        "message": f"{name}님 회원가입을 축하합니다.",
        "user_id": new_user.id,
        "age_group": age_group
    }), 200
