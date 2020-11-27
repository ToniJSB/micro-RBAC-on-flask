from app_flask.app.security.models import db, Permiso, Usuario, Rol
from app_flask.app import bcrypt
from sqlalchemy.sql import func

def get_all_permisos():
    return Permiso.query.all()
    
def filter_permisos_by_nombre_asc():
    return Permiso.query.order_by(Permiso.nombre.asc()) 

def filter_permisos_by_nombre_desc():
    return Permiso.query.order_by(Permiso.nombre.desc()) 

def filter_permisos_by_date_created_asc():
    return Permiso.query.order_by(Permiso.created_on.asc()) 

def filter_permisos_by_date_created_desc():
    return Permiso.query.order_by(Permiso.created_on.desc()) 

def filter_permisos_by_date_modified_asc():
    return Permiso.query.order_by(Permiso.changed_on.asc()) 

def filter_permisos_by_date_modified_desc():
    return Permiso.query.order_by(Permiso.changed_on.desc()) 

def filter_permisos_by_descripcion_asc():
    return Permiso.query.order_by(Permiso.descripcion.asc()) 

def filter_permisos_by_descripcion_desc():
    return Permiso.query.order_by(Permiso.descripcion.desc()) 

def get_permiso_by_id(id:int):
    return Permiso.query.filter(Permiso.id == id).first()



def get_all_usuarios():
    return Usuario.query.all()

def get_usuario_by_id(id:int):
    return Usuario.query.filter(Usuario.id == id).first()

def get_all_roles():
    return Rol.query.all()

def get_rol_by_id(id:int):
    return Rol.query.filter(Rol.id == id).first()


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
