from datetime import datetime
from app_flask.app.managment.models import Usuario
from app_flask.app import bcrypt
from app_flask.app.database import db

def get_all_usuarios():
    return Usuario.query.all()

def get_usuario_by_id(id:int):
    return Usuario.query.filter(Usuario.id == id)

def get_usuario_by_username(username:str):
    return Usuario.query.filter(Usuario.username == username)

def get_usuario_by_first_name_equals(first_name:str):
    return Usuario.query.filter(Usuario.first_name == first_name)
    
def get_usuario_by_last_name_equals(last_name:str):
    return Usuario.query.filter(Usuario.last_name == last_name)

def get_usuario_by_first_name_not_equals(first_name:str):
    return Usuario.query.filter(Usuario.first_name != first_name)

def get_usuario_by_last_name_not_equals(last_name:str):
    return Usuario.query.filter(Usuario.last_name != last_name)

def get_usuario_by_first_name_contains(first_name:str):

    return Usuario.query.filter(Usuario.first_name.contains(first_name))

def get_usuario_by_last_name_contains(last_name:str):
    return Usuario.query.filter(Usuario.last_name.contains(last_name))

def get_usuario_which_discharged():
    return Usuario.query.filter(Usuario.discharged != None)

def generate_usuario(user:Usuario):
    db.session.add(user)
    db.session.commit()

def update_usuario():    
    db.session.commit()

def delete_usuario(usuario):
    db.session.delete(usuario)
    db.session.commit()

def dischard_usuario(usuario):
    usuario.discharged = datetime.now()
    db.session.commit()