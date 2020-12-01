from flask import Blueprint,url_for,render_template, redirect
from flask.helpers import flash
from app_flask.app.security.models import db, Usuario
from app_flask.app import bcrypt 
main = Blueprint('main',__name__)
 
@main.route('/',methods=['GET'])
def home():
    return render_template('index.html')