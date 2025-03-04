from flask import Blueprint, jsonify, request, render_template, redirect

routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    return render_template('index.html')

@routes.route('/signup')
def signup():
    return render_template('signup.html')

@routes.route('/question')
def question():
    return render_template('question.html')

@routes.route('/result')
def result():
    return render_template('result.html')
