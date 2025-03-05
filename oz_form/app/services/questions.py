from flask import Blueprint, jsonify, request, abort
from app.models import db, Question, Choices
from sqlalchemy import func
import logging

logging.basicConfig(level=logging.DEBUG)

questions_blp = Blueprint("questions", __name__)

# 질문 가져오기
@questions_blp.route("/question/<int:question_id>", methods=["GET"])

def get_questions(question_id):
    question = Question.query.get_or_404(question_id)

    try :
        if not question :
            return jsonify({"error" : "질문을 찾을 수 없습니다"}),404
        
        choices = Choices.query.filter_by(question_id=question_id).all()

        choice_data = [{
                "id": choice.id, "content": choice.content, "is_active": choice.is_active
                }for choice in choices]
        
        return jsonify(
            {
                "id" : question.id,
                "title" : question.title,
                "image" : question.image.url if question.image else None,
                "chocies" : choice_data,
            }
        )
    except Exception as e:
        logging.error(f"Error: {str(e)}")
        abort(500,str(e))

# 질문 개수 확인
@questions_blp.route("/question/count", methods=["GET"])
def get_questions_count():
    # count = db.session.query(Question).count()  # 카운트
    count = db.session.query(func.count(Question.id)).scalar() # 
    return jsonify({"total": count})

# 질문 생성
@questions_blp.route("/question", methods=['POST'])
def create_questions():

    try:
        # JSON데이터 가져옴
        data = request.get_json()

        if not data or 'title' not in data or 'image_id' not in data:
            return jsonify({"error":"Missing required fields"}), 400
        
        # is_active를 bool 타입으로 변환
        is_active = data.get("is_active", True)  # 기본값 True 설정
        if isinstance(is_active, str):  # 문자열이면 변환
            is_active = is_active.lower() in ["true", "1", "yes"]  # "true", "1", "yes"는 True로 변환. 없으면 False

        # 새 질문 객체 생성
        new_question = Question(
            title = data['title'],
            is_active = is_active,
            sqe = int(data.get("sqe",1)),
            image_id=int(data["image_id"])
        )
        
        # 데이터베이스에 저장
        db.session.add(new_question)
        db.session.commit()
        
        return jsonify({"message": "Question created successfully", "question": new_question.to_dict()}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

# Request Body
# {
#     "title": "title",
#     "is_active": "True",
#     "sqe": "11",
#     "image_id": "10"
# }