from flask import Flask
from api.index import bp as index_bp
from api.board import bp as board_bp
from model import initialize_db


# 플라스크 앱 객체 할당
application = Flask(__name__)

# 플라스크 config 설정
application.config.update(
    DEBUG=True,                # 개발용 모드로 실행
    SECRET_KEY="super-secret", # 세션 암호화 시크릿 키
)

application.register_blueprint(index_bp)
application.register_blueprint(board_bp)

initialize_db()

if __name__ == '__main__':
    application.run(debug=True)
