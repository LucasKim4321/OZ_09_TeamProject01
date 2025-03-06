from flask import Blueprint, jsonify, request
from app.models import db, Answer

answers_blp = Blueprint('answers', __name__)

# 모든 답변 가져오기
@answers_blp.route('/result', methods=['GET'])
def get_all_answers():
    answers = Answer.query.all()

    result = [{"user_id":answer.user_id , "choice_id":answer.choice_id} for answer in answers]

    try:
        return jsonify(result)
    except AttributeError:
        return jsonify({"error":"invalid question data"}), 500

# 특정 유저의 모든 답변 가져오기
@answers_blp.route('/result/<int:user_id>', methods=['GET'])
def get_answers(user_id):
    answers = Answer.query.all()

    result = [answer.to_dict() for answer in answers]

    try:
        return jsonify(result)
    except AttributeError:
        return jsonify({"error":"invalid question data"}), 500
    
# 답변 등록
@answers_blp.route('/submit', methods=['POST'])
def post_answers():
    try:
        # JSON데이터 가져옴
        data = request.get_json()

        if not data or len(data) == 0:
            return jsonify({"error":"Missing required fields"}), 400
        
        # 결과 등록 전 특정 유저의 기존 데이터 삭제
        # 첫 번째 데이터에서 user_id 가져오기
        # user_id = int(data[0]['user_id'])
        # 기존 데이터 삭제 (해당 user_id를 가진 모든 답변 삭제)
        # Answer.query.filter_by(user_id=user_id).delete()
        
        # 결과 등록 전 모든 기존 데이터 삭제
        Answer.query.delete()
        
        db.session.commit()
        
        for answer in data:

            # 새 대답 객체 생성
            new_answer = Answer(
                user_id = int(answer['user_id']),
                choice_id = int(answer['choice_id'])
            )
            
            # 데이터베이스에 저장
            db.session.add(new_answer)
        
        db.session.commit()
        
        return jsonify({"message": "Question created successfully"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    
# Request Body
# [
#   { "user_id": 1, "choice_id": 2 },
#   { "user_id": 1, "choice_id": 4 }
# ]