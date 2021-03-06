import os

class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    ENV = 'development'
    
    # Setup default language
    BABEL_DEFAULT_LOCALE = "es"
    # Your application default translation path
    BABEL_DEFAULT_FOLDER = "translations"
    # The allowed translation for you app
    LANGUAGES = {
        "es": {"flag": "es", "name": "Spanish"},
        "en": {"flag": "gb", "name": "English"},
    }