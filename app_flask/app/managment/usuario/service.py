from app_flask.app.database.daoPermiso import get_all_permisos
from app_flask.app.database.daoRol import get_all_roles
from app_flask.app.database.daoUsuario import *
from app_flask.app.managment.models import Usuario

def find_all_usuarios():
    """
    Solicita a la capa de persistencia todos los usuarios
    """
    return get_all_usuarios()

def create_usuario(form):
    """
    Solicita a la capa de persistencia crear un usuario
    
    Parametros
    -
    FlaskForm
    """
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
    """
    Recibe por parámetro la id del rol a borrar
    """
    user = get_usuario_by_id(id)
    discharg = False
    for permiso in get_all_permisos():
        if permiso.changed_by == user or permiso.created_by == user:
            discharg = True
            break
    for rol in get_all_roles():
        if rol.changed_by == user or rol.created_by == user:
            discharg = True
            break
    if discharg:
        dischard_usuario(user)
    else:
        delete_usuario(user)
    pass