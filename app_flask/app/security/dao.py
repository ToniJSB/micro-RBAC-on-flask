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

def update_permiso(id, form):
    permisoG = get_permiso_by_id(id)
    permisoG.nombre = form.nombre.data
    permisoG.descripcion = form.descripcion.data
    db.session.commit()

def delete_permiso(id):
    perm = get_permiso_by_id(id)
    db.session.delete(perm)
    db.session.commit()

def create_rol(rol:Rol):
    db.session.add(rol)
    db.session.commit()

def update_rol(id,form):
    rolG = get_rol_by_id(id)
    rolG.nombre = form.nombre.data
    rolG.descripcion = form.descripcion.data
    rolG.permisos = form.permisos.data
    
    db.session.commit()

def delete_rol(id):
    rol = get_rol_by_id(id)
    db.session.delete(rol)
    db.session.commit()

def create_usuario(user:Usuario):
    ownId = db.engine.execute('select max(id) from usuario')
    laid = [row[0] for row in ownId]
    print(laid)
    if laid[0] == None:
        laid[0] = 0

    user.created_by_fk = laid[0] + 1
    user.changed_by_fk = laid[0] + 1

    db.session.add(user)
    db.session.commit()

def update_usuario(id,form):
    usuarioG = get_usuario_by_id(id)
    usuarioG.username = form.username.data
    usuarioG.first_name = form.first_name.data
    usuarioG.last_name = form.last_name.data
    usuarioG.roles = form.roles.data
    print(form.password.data)
    if form.password.data != '' and form.confirm_password.data != '' and form.confirm_password.data == form.password.data :
        usuarioG.password = bcrypt.generate_password_hash(form.password.data)
    db.session.commit()

def delete_usuario(id):
    user = get_usuario_by_id(id)
    print(user)
    db.session.delete(user)
    db.session.commit()