from app_flask.app.database.daoPermiso import *
from app_flask.app.managment.models import Permiso
from app_flask.app.database import remove_extra_attr


def find_all_permisos():
    """
    Solicita a la capa de persistencia todos los permisos
    """
    permisos = []
    attr = []
    for permiso in get_all_permisos():
        permiso.__dict__.pop('rol')
        remove_extra_attr(permiso)
        if attr == []:
            attr = list(permiso.__dict__.keys())
            attr.append('buttons')
            
        permisos.append(permiso.__dict__)
    obj = {
        'attr': attr,
        'lista':permisos 
    }
    return obj

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

def modify_permiso(id,form):
    permisoG = get_permiso_by_id(id)[0]
    
    permisoG.nombre = form.nombre.data
    permisoG.descripcion = form.descripcion.data
    update_permiso(permisoG)
    pass

def find_permisos_by(attr,simil,text):
    """
    Solicita a la capa de persistencia permisos
    rigiendose en los parámetros que le envian
    
    Parametros
    -
    :param:`attr:` el atributo por el que queremos buscar\n
    :param:`simil:` el tipo de filtrado que deseamos.\n
        \tP.E: EQUAL,NOTEQUAL,CONTAINS
    :param:`text:` el texto por el que queremos filtrar
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
    delete_permiso(permiso[0])
    pass