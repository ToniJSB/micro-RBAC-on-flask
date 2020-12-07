from app_flask.app.database.daoUsuario import *
from app_flask.app.managment.models import Usuario

def find_all_usuarios():
    return get_all_usuarios()

def create_usuario(form):
    hashed_pass = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    user = Usuario(username=form.username.data,first_name=form.first_name.data,last_name=form.last_name.data,password=hashed_pass,roles=form.roles.data)
    generate_usuario(user)
    return user

def find_usuario_by_username(username):
    return get_usuario_by_username(username)
def find_usuario_by_id(id):
    return get_usuario_by_id()

def auth_delete_usuario(id):
    user = get_usuario_by_id(id)
    if len(user.roles) >= 0:
    
        return True
    return False
    

def confirm_delete_usuario(id):
    user = get_usuario_by_id(id)
    user_roles = user.roles
    user_roles.clear()
    print(user.id)
    print(user.username )
    print(user.first_name)
    delete_usuario(user)
    pass