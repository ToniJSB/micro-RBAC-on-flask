from flask import Blueprint
from app_flask.app.main.routes import home

main = Blueprint('main',__name__)

main.add_url_rule('/',view_func=home,methods=['GET'])
