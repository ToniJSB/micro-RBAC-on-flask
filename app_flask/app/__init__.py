from app_flask.app.config import Config
from flask import Flask, current_app, request
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_babel import Babel

manager_login = LoginManager()
bcrypt = Bcrypt()
babel = Babel()

def create_app(test_config=None):
    """ Genera una instancia de la aplicación """
    app = Flask(__name__)
    app.config.from_object(Config)
    
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    from app_flask.app.database import db

    db.init_app(app)
    bcrypt.init_app(app)
    manager_login.init_app(app)
    babel.init_app(app)


    from app_flask.app.main import main
    from app_flask.app.login import auth
    from app_flask.app.managment import managment
    from app_flask.app.cli import gen, translate

    app.register_blueprint(main)
    app.register_blueprint(auth)
    app.register_blueprint(managment)
    app.register_blueprint(gen)
    app.register_blueprint(translate)

    return app
        
app = create_app()