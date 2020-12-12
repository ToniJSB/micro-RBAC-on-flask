from flask import render_template

from app_flask.app.database.utils import  load_user

 
def home():
    load_user
    return render_template('index.html')