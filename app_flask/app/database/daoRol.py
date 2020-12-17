from app_flask.app.managment.models import Rol
from app_flask.app.database import db


def get_all_roles():
    return Rol.query.all()

def get_rol_by_id(id:int):
    return Rol.query.filter(Rol.id == id)

def get_rol_by_nombre(nombre):
    return Rol.query.filter(Rol.nombre == nombre)

def get_rol_by_descripcion_equals(descripcion:str):
    return Rol.query.filter(Rol.descripcion == descripcion)

def get_rol_by_descripcion_not_equals(descripcion:str):
    return Rol.query.filter(Rol.descripcion != descripcion)

def get_rol_by_descripcion_contains(descripcion:str):
    return Rol.query.filter(Rol.descripcion.contains(descripcion))

def generate_rol(rol:Rol):
    db.session.add(rol)
    db.session.commit()

def update_rol(rol):
    db.session.commit()

def delete_rol(rol):
    
    db.session.delete(rol)
    db.session.commit()