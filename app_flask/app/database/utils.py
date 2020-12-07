from app_flask.app import manager_login
from app_flask.app.managment.models import Usuario

@manager_login.user_loader
def load_user(id):
    return Usuario.query.get(int(id))

