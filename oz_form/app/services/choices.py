from flask import Blueprint, request, jsonify
from app.models import db, Choices

choices_blp = Blueprint('choices', __name__)

@choices_blp.route('/choice/<int:question_id>', methods=['GET'])
def get_choices(question_id):
    choices = Choices.query.filter_by(question_id=question_id).all()
    
    if not choices:
        return jsonify({"message": "선택지를 찾을 수 없습니다."}), 404

    return jsonify([choice.to_dict() for choice in choices])

@choices_blp.route('/choice', methods=['POST'])
def create_choice():
    data = request.get_json()

    if not data or 'question_id' not in data or 'content' not in data or 'sqe' not in data:
        return jsonify({"error": "올바른 데이터 형식이 아닙니다."}), 400

    new_choice = Choices(
        question_id=data['question_id'],
        content=data['content'],
        is_active=True,
        sqe=data['sqe']
    )
    db.session.add(new_choice)
    db.session.commit()

    return jsonify({"message": f"Content: {new_choice.content} choice Success Create"}), 201
