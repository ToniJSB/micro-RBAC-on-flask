from app_flask.app.security.models import db, Permiso, Usuario, Rol
from app_flask.app import bcrypt
from sqlalchemy.sql import func

def get_all_permisos():
    return Permiso.query.all()
    

def create_permiso(perm:Permiso):
    db.session.add(perm)
    db.session.commit()

def create_rol(rol:Rol):
    db.session.add(rol)
    db.session.commit()

def create_usuario(user:Usuario):
    persid = Usuario.query.order_by(Usuario.id.desc()).first()

    user.created_by_fk = persid.id + 1
    user.changed_by_fk = persid.id + 1

    db.session.add(user)
    db.session.commit()
