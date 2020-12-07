from app_flask.app.database.daoPermiso import *
from app_flask.app.managment.models import Permiso


def find_all_permisos():
    return get_all_permisos()

def create_permiso(form):
    permiso = Permiso(nombre=form.nombre.data,descripcion=form.descripcion.data)
    generate_permiso(permiso)
    return permiso

def find_permiso_by_nombre(nombre):
    return get_permiso_by_nombre(nombre)

def find_permiso_by_id(id):
    return get_permiso_by_id(id)

def auth_delete_permiso(id):
    return True
    
def confirm_delete_permiso(id):
    permiso = get_permiso_by_id(id)
    delete_permiso(permiso)
    pass