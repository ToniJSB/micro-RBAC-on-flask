from flask import render_template, current_app

from app_flask.app.database.utils import  load_user
from app_flask.app.managment.utils import  get_languages

 
def home():
    load_user
    
    return render_template('index.html',lang = get_languages())