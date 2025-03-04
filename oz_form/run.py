from app import create_app, db

application = create_app()

if __name__ == "__main__":

    # 처음 한번 실행시 테이블 생성
    # with application.app_context():
    #     db.create_all()

    # flask db init 초기화 (처음 한번만)
    # flask db migrate  마이그레이션 생성
    # flask db migrate -m "message"
    # flask db upgrade  생성된 마이그레이션 적용. 업그레이드
    # flask db downgrade 이전 마이그레이션 상태로. 다운그레이드

    application.run(debug=True)