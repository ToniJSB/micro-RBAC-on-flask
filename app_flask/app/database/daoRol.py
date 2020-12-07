from app_flask.app.managment.models import Rol
from app_flask.app.database import db


def get_all_roles():
    return Rol.query.all()

def get_rol_by_id(id:int):
    return Rol.query.filter(Rol.id == id).first()

def get_rol_by_nombre(nombre):
    return Rol.query.filter(Rol.nombre == nombre).first()

def generate_rol(rol:Rol):
    db.session.add(rol)
    db.session.commit()

def update_rol(id,form):
    rolG = get_rol_by_id(id)
    rolG.nombre = form.nombre.data
    rolG.descripcion = form.descripcion.data
    rolG.permisos = form.permisos.data
    
    db.session.commit()

def delete_rol(rol):
    
    db.session.delete(rol)
    db.session.commit()