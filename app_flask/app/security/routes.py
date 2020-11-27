from operator import ge
from flask.globals import request
from flask_login.utils import login_required
from app_flask.app.security.dao import create_permiso, create_rol, create_usuario, filter_permisos_by_nombre_desc, get_permiso_by_id, get_rol_by_id,get_usuario_by_id, get_all_roles, get_all_usuarios
from flask import Blueprint,url_for,render_template, redirect, json
from flask.helpers import flash
from .forms import RegisterPermisoForm, RegisterRolForm, RegisterUsuarioForm, UpdateUsuarioForm
from app_flask.app.security.models import db, Permiso, Usuario, Rol
from app_flask.app import bcrypt,manager_login


create = Blueprint('create',__name__,url_prefix='/create/')

@create.route('/usuario', methods=['GET','POST'])
def c_usuario():
    form = RegisterUsuarioForm()
    if form.validate_on_submit():
        hashed_pass = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = Usuario(username=form.username.data,first_name=form.first_name.data,last_name=form.last_name.data,password=hashed_pass,roles=form.roles.data)
        create_usuario(user)
        flash('account created for '+ user.username + '!', 'success')
        return redirect(url_for('auth.login'))
    
    return render_template('registerUsuario.html', form=form)

@create.route('/permiso', methods=['GET','POST'])
@login_required
def c_permiso():
    form = RegisterPermisoForm()
    
    if form.validate_on_submit():
        permiso = Permiso(nombre=form.nombre.data,descripcion=form.descripcion.data)
        create_permiso(permiso)
        flash('permiso creado: '+permiso.nombre+'!', 'success')
        return redirect(url_for('main.home'))
    return render_template('registerPermiso.html',form=form)

@create.route('/rol', methods=['GET','POST'])
@login_required
def c_rol():
    form = RegisterRolForm()
    if form.validate_on_submit():
        print(form.permisos)
        rol = Rol(nombre=form.nombre.data,descripcion=form.descripcion.data,permisos=form.permisos.data)
        create_rol(rol)
        flash('rol created: '+rol.nombre+'!','success')
        return redirect(url_for('main.home'))
    return render_template('registerRol.html', form=form)



view = Blueprint('view',__name__,url_prefix='/view/')

@view.route('/permiso')
@login_required
def v_permiso():
    permisos_n = filter_permisos_by_nombre_desc()
    attr=list(permisos_n[0].__dict__.keys())
    attr.pop(0)
    attr.insert(0,'buttons')
    return render_template('viewBase.html',attr=attr,obj=permisos_n, title='permiso')
    
@view.route('/rol')
@login_required
def v_rol():
    roles = get_all_roles()
    print(roles)
    attr=list(roles[0].__dict__.keys())
    attr.pop(0)
    attr.insert(0,'buttons')
    print(attr)
    return render_template('viewBase.html',attr=attr,obj=roles,title='rol')
    


@view.route('/usuario')
@login_required
def v_usuario():
    usuarios = get_all_usuarios()
    attr=list(usuarios[0].__dict__.keys())
    
    attr.pop(0)
    attr.sort()

    attr.pop(len(attr)-2)
    attr.insert(0,'buttons')
    
    return render_template('viewBase.html',attr=attr,obj=usuarios,title='usuario')

update = Blueprint('update',__name__, url_prefix='/update/')

@update.route('/permiso/<int:id>', methods=['GET','POST'])
@login_required
def u_permiso(id):
    permisoG = get_permiso_by_id(id)
    form = RegisterPermisoForm()
    if form.validate_on_submit():
        permisoG.nombre = form.nombre.data
        permisoG.descripcion = form.descripcion.data
        print(permisoG)
        db.session.commit()
        flash('el permiso ha sido modificado','success')
        return redirect(url_for('view.v_permiso'))

    elif request.method == 'GET':
       form.nombre.data = permisoG.nombre 
       form.descripcion.data = permisoG.descripcion 
    
    return render_template('registerPermiso.html', form=form)

@update.route('/rol/<int:id>', methods=['GET','POST'])
@login_required
def u_rol(id):
    rolG = get_rol_by_id(id)
    form = RegisterRolForm()
    if form.validate_on_submit():
        rolG.nombre = form.nombre.data
        rolG.descripcion = form.descripcion.data
        rolG.permisos = form.permisos.data
        print(rolG)
        db.session.commit()
        flash('el rol ha sido modificado','success')
        return redirect(url_for('view.v_rol'))

    elif request.method == 'GET':
       form.nombre.data = rolG.nombre 
       form.descripcion.data = rolG.descripcion 
       form.permisos.data = rolG.permisos
    
    return render_template('registerrol.html', form=form)

@update.route('/usuario/<int:id>', methods=['GET','POST'])
@login_required
def u_usuario(id):
    usuarioG = get_usuario_by_id(id)
    form = UpdateUsuarioForm()
    if form.validate_on_submit():
        usuarioG.username = form.username.data
        usuarioG.first_name = form.first_name.data
        usuarioG.last_name = form.last_name.data
        usuarioG.roles = form.roles.data
        if form.confirm_password.data == form.password:
            usuarioG.password = bcrypt.generate_password_hash(form.password.data)
        print(usuarioG.password)
        db.session.commit()
        flash('el usuario ha sido modificado','success')
        return redirect(url_for('view.v_usuario'))

    elif request.method == 'GET':
        form.username.data = usuarioG.username 
        form.first_name.data = usuarioG.first_name 
        form.last_name.data = usuarioG.last_name
        form.roles.data = usuarioG.roles
    
    return render_template('registerUsuario.html', form=form)