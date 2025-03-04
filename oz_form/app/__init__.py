from flask import Flask, jsonify
from flask_migrate import Migrate

import app.models
from app.routes import routes
from app.services.users import users_bp
from app.services.questions import questions_blp
from app.services.choices import choices_blp
from config import db

migrate = Migrate()


def create_app():
    application = Flask(__name__)

    application.config.from_object("config.Config")
    application.secret_key = "oz_form_secret"

    db.init_app(application)

    migrate.init_app(application, db)

		# 400 에러 발생 시, JSON 형태로 응답 반환
    @application.errorhandler(400)
    def handle_bad_request(error):
        response = jsonify({"message": error.description})
        response.status_code = 400
        return response

		# 블루프린트 등록
    application.register_blueprint(routes)
    application.register_blueprint(users_bp)
    application.register_blueprint(questions_blp)
    application.register_blueprint(choices_blp)


    return application