from app_flask.app.database.daoRol import *
from app_flask.app.managment.models import Rol

def find_all_roles():
    return get_all_roles()

def create_rol(form):
    print(form.nombre.data)
    print(form.descripcion.data)
    print(form.permisos.data)
    rol = Rol(nombre=form.nombre.data,descripcion=form.descripcion.data,permisos=form.permisos.data)
    generate_rol(rol)
    return rol

def find_rol_by_id(id):
    return get_rol_by_id(id)

def find_rol_by_nombre(nombre):
    return get_rol_by_nombre(nombre)

def auth_delete_rol(id):
    return True

def confirm_delete_rol(id):
    rol = get_rol_by_id(id)
    rol.permisos.clear()
    delete_rol(rol)
    pass