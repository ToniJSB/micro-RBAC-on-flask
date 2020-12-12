import os
from flask import Flask, current_app, request
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_babel import Babel

manager_login = LoginManager()
bcrypt = Bcrypt()
babel = Babel()

def create_app():
    """ Genera una instancia de la aplicación """
    app = Flask(__name__)


    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

    app.config['DEBUG'] = True
    app.config['ENV'] = 'development'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///modelodb.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    from app_flask.app.database import db

    db.init_app(app)
    manager_login.init_app(app)
    babel.init_app(app)
    from app_flask.app.main import main
    from app_flask.app.login import auth
    from app_flask.app.managment import managment
    from app_flask.app.generate import gen

    app.register_blueprint(main)
    app.register_blueprint(auth)
    app.register_blueprint(managment)
    app.register_blueprint(gen)

    return app
        
app = create_app()