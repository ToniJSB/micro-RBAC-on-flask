from app_flask.app.managment.models import Usuario
from app_flask.app import bcrypt
from app_flask.app.database import db

def get_all_usuarios():
    return Usuario.query.all()

def get_usuario_by_username(username:str):
    return Usuario.query.filter(Usuario.username == username).first()

def get_usuario_by_id(id:int):
    return Usuario.query.filter(Usuario.id == id).first()

def generate_usuario(user:Usuario):
    ownId = db.engine.execute('select max(id) from usuario')
    laid = [row[0] for row in ownId]
    print(laid)
    if laid[0] == None:
        laid[0] = 0

    user.created_by_fk = laid[0] + 1
    user.changed_by_fk = laid[0] + 1

    db.session.add(user)
    db.session.commit()

def update_usuario():    
    db.session.commit()

def delete_usuario(usuario):
    db.session.delete(usuario)
    db.session.commit()