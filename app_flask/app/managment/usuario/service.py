from app_flask.app.database import remove_extra_attr
from app_flask.app.database.daoPermiso import get_all_permisos
from app_flask.app.database.daoRol import get_all_roles,get_rol_by_id
from app_flask.app.database.daoUsuario import *
from app_flask.app.managment.models import Usuario

def find_all_usuarios(lista=[]):
    """
    Solicita a la capa de persistencia todos los usuarios
    """
    usuarios = []
    attr = []
    if lista != []:
        for usuario in lista:
            if attr == []:
                attr = list(usuario.keys())
                attr.append('buttons')
                usuarios = lista
                break
    else:
        for usuario in get_all_usuarios():
            remove_extra_attr(usuario)
            if attr == []:
                attr = list(usuario.__dict__.keys())
                attr.append('buttons')

            usuarios.append(usuario.__dict__)

    obj = {
        'attr': attr,
        'lista':usuarios
    }

    return obj

def create_usuario(form):
    """
    Solicita a la capa de persistencia crear un usuario
    
    Parametros
    -
    FlaskForm
    """
    rolesId = form.list_options.raw_data
    roles = []
    for rol in rolesId:
        roles.append(get_rol_by_id(int(rol))[0])

    hashed_pass = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    user = Usuario(username=form.username.data,first_name=form.first_name.data,last_name=form.last_name.data,password=hashed_pass,roles=roles)
    generate_usuario(user)
    return user

def modify_usuario(id,form):
    rolesId = form.list_options.raw_data
    roles = []
    for rol in rolesId:
        roles.append(get_rol_by_id(int(rol))[0])

    usuarioG = get_usuario_by_id(id)
    usuarioG.username = form.username.data
    usuarioG.first_name = form.first_name.data
    usuarioG.last_name = form.last_name.data
    usuarioG.roles = roles

    if form.password.data != '' and form.confirm_password.data != '' and form.confirm_password.data == form.password.data :
        usuarioG.password = bcrypt.generate_password_hash(form.password.data)
    update_usuario()


def find_usuario_by_username(username):
    return get_usuario_by_username(username)
def find_usuario_by_id(id):
    return get_usuario_by_id(id)

def find_usuarios_by(attr,simil,text):
    """
    Solicita a la capa de persistencia usuarios
    rigiendose en los parámetros que le envian
    
    Parametros
    -
    :param:`attr:` el atributo por el que queremos buscar\n
    :param:`simil:` el tipo de filtrado que deseamos.\n
        \tP.E: EQUAL,NOTEQUAL,CONTAINS
    :param:`text:` el texto por el que queremos filtrar
    """
    if attr == 'id' or attr == 'username':
        if attr == 'username':
            return list(get_usuario_by_username(text))
        else:
            return list(get_usuario_by_id(text))
    elif attr == 'first_name':
        if simil == 'equal':
            return list(get_usuario_by_first_name_equals(text))
        elif simil == 'notequal':
            return list(get_usuario_by_first_name_not_equals(text))
        elif simil == 'contains':
            return list(get_usuario_by_first_name_contains(text))
    elif attr == 'last_name':
        if simil == 'equal':
            return list(get_usuario_by_last_name_equals(text))
        elif simil == 'notequal':
            return list(get_usuario_by_last_name_not_equals(text))
        elif simil == 'contains':
            return list(get_usuario_by_last_name_contains(text))
    elif attr == 'discharged':
        return list(get_usuario_which_discharged())

def auth_delete_usuario(id):
    user = get_usuario_by_id(id)[0]
    if len(user.roles) >= 0:
        return True
    return False
    

def confirm_delete_usuario(id):
    """
    Recibe por parámetro la id del rol a borrar
    """
    user = get_usuario_by_id(id)[0]
    discharg = False
    for permiso in get_all_permisos():
        if permiso.changed_by == user or permiso.created_by == user:
            discharg = True
            break
    for rol in get_all_roles():
        if rol.changed_by == user or rol.created_by == user:
            discharg = True
            break
    if discharg:
        dischard_usuario(user)
    else:
        delete_usuario(user)
    pass