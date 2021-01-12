from flask import Blueprint
from app_flask.app.login.routes import login, logout

auth = Blueprint('auth',__name__)

auth.add_url_rule('/login',methods=['GET','POST'],view_func=login)
auth.add_url_rule('/logout',methods=['GET'],view_func=logout)