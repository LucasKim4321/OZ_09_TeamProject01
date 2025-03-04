from flask import Blueprint, jsonify, request, render_template, redirect, flash, url_for
from app.models import db, User, AgeStatus, GenderStatus

routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    return render_template('index.html')

@routes.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template('signup.html')

@routes.route('/question/<int:question_id>')
def question(question_id):
    return render_template('question.html', question_id=question_id)

@routes.route('/result')
def result():
    return render_template('result.html')
