from flask import Flask

application = Flask(__name__)
application.config.update(
    DEBUG=True,
    SECRET_KEY="super-secret"
)