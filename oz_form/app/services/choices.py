from flask import Blueprint, jsonify
from app.models import db, Choices

choices_blp = Blueprint('choices', __name__)

@choices_blp.route('/choice/<int:question_id>', methods=['GET'])
def get_choices(question_id):
    choices = Choices.query.get_or_404(question_id)
    print(choices)

    return jsonify(choices.to_dict())
