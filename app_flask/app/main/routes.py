from flask import render_template

from app_flask.app.database.utils import  load_user
from app_flask.app.database import  create_db

 
def home():
    load_user
    return render_template('index.html')