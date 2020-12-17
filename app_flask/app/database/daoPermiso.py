from app_flask.app.managment.models import Permiso
from app_flask.app.database import db


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
    return Permiso.query.filter(Permiso.id == id)

def get_permiso_by_nombre(nombre:str):
    return Permiso.query.filter(Permiso.nombre == nombre)

def get_permisos_by_descripcion_equals(descripcion:str):
    return Permiso.query.filter(Permiso.descripcion == descripcion)
    
def get_permisos_by_descripcion_not_equals(descripcion:str):
    return Permiso.query.filter(Permiso.descripcion != descripcion)

def get_permisos_by_descripcion_contains(descripcion:str):
    return Permiso.query.filter(Permiso.descripcion.contains(descripcion))



def generate_permiso(perm:Permiso):
    db.session.add(perm)
    db.session.commit()

def update_permiso(perm):
    db.session.commit()

def delete_permiso(perm):
    db.session.delete(perm)
    db.session.commit()
