import os

from flask import Flask, current_app, request
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

manager_login = LoginManager()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

    app.config['DEBUG'] = True
    app.config['ENV'] = 'development'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///modelodb.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    from app_flask.app.security.models import db

    db.init_app(app)
    manager_login.init_app(app)

    from .main.routes import main
    from .login.routes import auth
    from .security.routes import create, view, update

    app.register_blueprint(main)
    app.register_blueprint(auth)
    app.register_blueprint(create)
    app.register_blueprint(view)
    app.register_blueprint(update)

    return app
