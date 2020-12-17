from app_flask.app.database import remove_extra_attr
from app_flask.app.database.daoRol import *
from app_flask.app.database.daoPermiso import get_permiso_by_id
from app_flask.app.managment.models import Permiso, Rol

def find_all_roles():
    """
    Solicita a la capa de persistencia todos los roles
    """
    roles = []
    attr = []
    for rol in get_all_roles():
        rol.__dict__.pop('usuario')
        remove_extra_attr(rol)
        
        if attr == []:
            
            attr = list(rol.__dict__.keys())
            attr.append('buttons')
            # if rol.__dict__.get('usuario') != []:
            #     
            #     for usuario in rol.__dict__.get('usuario'):
            #         remove_extra_attr(usuario)
            #         usuarios.append(usuario.__dict__)
            #     print(usuarios)
            #     rol.__dict__['usuario'] = usuarios
        roles.append(rol.__dict__)
    obj = {
        'attr': attr,
        'lista':roles
    }
    return obj

def create_rol(form):
    """
    Solicita a la capa de persistencia crear un rol
    
    Parametros
    -
    FlaskForm
    """
    permisosId = form.list_options.raw_data
    permisos = []
    for perm in permisosId:
        permisos.append(get_permiso_by_id(int(perm))[0])
    
    rol = Rol(nombre=form.nombre.data,descripcion=form.descripcion.data,permisos=permisos)
    generate_rol(rol)
    return rol

def modify_rol(id,form):
    permisosId = form.list_options.raw_data
    
    permisos = []
    for perm in permisosId:
        permisos.append(get_permiso_by_id(int(perm))[0])
    
    rolG = get_rol_by_id(id)[0]
    rolG.nombre = form.nombre.data
    rolG.descripcion = form.descripcion.data
    rolG.permisos = permisos
    update_rol(rolG)
    pass

def find_rol_by_id(id):
    return get_rol_by_id(id)

def find_rol_by_nombre(nombre):
    return get_rol_by_nombre(nombre)

def find_roles_by(attr,simil,text):
    """
    Solicita a la capa de persistencia roles
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
            return list(get_rol_by_nombre(text))
        else:
            return list(get_rol_by_id(text))
    elif attr == 'descripcion':
        if simil == 'equal':
            return list(get_rol_by_descripcion_equals(text))
        elif simil == 'notequal':
            return list(get_rol_by_descripcion_not_equals(text))
        elif simil == 'contains':
            return list(get_rol_by_descripcion_contains(text))
    

def auth_delete_rol(id):
    return True

def confirm_delete_rol(id):
    """
    Recibe por parámetro la id del rol a borrar
    """
    rol = get_rol_by_id(id)
    rol.permisos.clear()
    delete_rol(rol)
    pass