from app_flask.app.database.daoPermiso import *
from app_flask.app.managment.models import Permiso


def find_all_permisos():
    """
    Solicita a la capa de persistencia todos los permisos
    """
    return get_all_permisos()

def create_permiso(form):
    """
    Solicita a la capa de persistencia crear un permiso
    
    Parametros
    -
    FlaskForm
    """
    permiso = Permiso(nombre=form.nombre.data,descripcion=form.descripcion.data)
    generate_permiso(permiso)
    return permiso


def find_permisos_by(attr,simil,text):
    """
    Solicita a la capa de persistencia permisos
    rigiendose en los parámetros que le envian
    
    Parametros
    -
    :param:`attr:` el atributo por el que queremos buscar\n
    :param:`simil:` el tipo de filtrado que deseamos.\n
        \tP.E: EQUAL,NOT_EQUAL,CONTAINS
    """
    if attr == 'id' or attr == 'nombre':
        if attr == 'nombre':
            return list(get_permiso_by_nombre(text))
        else:
            return list(get_permiso_by_id(text))
    else:
        if simil == 'equal':
            return list(get_permisos_by_descripcion_equals(text))
        elif simil == 'notequal':
            return list(get_permisos_by_descripcion_not_equals(text))
        elif simil == 'contains':
            return list(get_permisos_by_descripcion_contains(text))
    

def auth_delete_permiso(id):
    return True
    
def confirm_delete_permiso(id):
    """
    Recibe por parámetro la id del permiso a borrar
    """
    permiso = get_permiso_by_id(id)
    delete_permiso(permiso)
    pass