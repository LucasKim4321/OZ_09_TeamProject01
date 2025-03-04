from flask import Blueprint, jsonify
from app.models import db, Question, Choices

questions_blp = Blueprint("questions", __name__)

@questions_blp.route("/questions/<int:question_id>", methods=["GET"])
def get_questions(question_id):
    question = Question.query.get_or_404(question_id)

    return jsonify(question.to_dict())


@questions_blp.route("/questions/count", methods=["GET"])
def get_questions_count():
    count = db.session.query(Question).count()  # 카운트
    return jsonify({"total": count})
