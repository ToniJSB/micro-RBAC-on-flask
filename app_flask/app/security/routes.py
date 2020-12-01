from operator import ge
from warnings import resetwarnings
from flask.globals import request
from flask_login.utils import login_required
from app_flask.app.security.dao import create_permiso, create_rol, create_usuario, delete_permiso, get_all_permisos, get_rol_by_id,get_usuario_by_id, get_all_roles, get_all_usuarios, update_permiso, get_permiso_by_id, update_rol, update_usuario, delete_rol,delete_usuario
from flask import Blueprint,url_for,render_template, redirect, json
from flask_login import current_user
from flask.helpers import flash
from .forms import RegisterPermisoForm, RegisterRolForm, RegisterUsuarioForm, UpdateUsuarioForm
from app_flask.app.security.models import db, Permiso, Usuario, Rol
from app_flask.app import bcrypt,manager_login


create = Blueprint('create',__name__,url_prefix='/create/')

@create.route('/usuario', methods=['GET','POST'])
@manager_login.unauthorized_handler
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
    permisos_n = get_all_permisos()    
    if len(permisos_n)==0:
        return redirect(url_for('create.c_permiso'))
        
    attr=list(permisos_n[0].__dict__.keys())
    attr.pop(0)
    attr.insert(0,'buttons')
    return render_template('viewBase.html',attr=attr,obj=permisos_n, title='permiso')
    
@view.route('/rol')
@login_required
def v_rol():
    roles = get_all_roles()
    if len(roles) == 0:
        return redirect(url_for('create.c_rol'))
    
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
    form = RegisterPermisoForm()
    if form.validate_on_submit():
        update_permiso(id, form)
        flash('el permiso ha sido modificado','success')
        return redirect(url_for('view.v_permiso'))

    elif request.method == 'GET':
        permisoG = get_permiso_by_id(id)
        form.nombre.data = permisoG.nombre 
        form.descripcion.data = permisoG.descripcion 
    
    return render_template('registerPermiso.html', form=form)

@update.route('/rol/<int:id>', methods=['GET','POST'])
@login_required
def u_rol(id):
    form = RegisterRolForm()
    if form.validate_on_submit():
        update_rol(id, form)
        flash('el rol ha sido modificado','success')
        return redirect(url_for('view.v_rol'))

    elif request.method == 'GET':
        rolG = get_rol_by_id(id)
        form.nombre.data = rolG.nombre 
        form.descripcion.data = rolG.descripcion 
        form.permisos.data = rolG.permisos
    
    return render_template('registerrol.html', form=form)

@update.route('/usuario/<int:id>', methods=['GET','POST'])
@login_required
def u_usuario(id):
    form = UpdateUsuarioForm()
    if form.validate_on_submit():
        print(form.password.data)
        update_usuario(id,form)
        flash('el usuario ha sido modificado','success')
        return redirect(url_for('view.v_usuario'))

    elif request.method == 'GET':
        usuarioG = get_usuario_by_id(id)
        form.username.data = usuarioG.username 
        form.first_name.data = usuarioG.first_name 
        form.last_name.data = usuarioG.last_name
        form.roles.data = usuarioG.roles
    
    return render_template('registerUsuario.html', form=form)

delete = Blueprint('delete',__name__,url_prefix='/delete/')

@delete.route('/permiso/<int:id>',methods=['GET'])
@login_required
def d_permiso(id):
    delete_permiso(id)
    return redirect(url_for('view.v_permiso'))

@delete.route('/rol/<int:id>',methods=['GET'])
@login_required
def d_rol(id):
    delete_rol(id)
    return redirect(url_for('view.v_rol'))

@delete.route('/usuario/<int:id>',methods=['GET'])
@login_required
def d_usuario(id):
    delete_usuario(id)
    return redirect(url_for('view.v_usuario'))

show = Blueprint('show',__name__,url_prefix='/show/')

@show.route('/permiso/<int:id>')
@login_required
def s_permiso(id):
    permiso = get_permiso_by_id(id)
    perm = list(permiso.__dict__.items())
    perm.pop(0)
    perm.sort(reverse=True)
    return render_template('showBase.html',title='permiso',obj=perm)

@show.route('rol/<int:id>')
@login_required
def s_rol(id):
    role = get_rol_by_id(id)
    rol = list(role.__dict__.items())
    rol.pop(0)
    rol.sort(reverse=True)
    return render_template('showBase.html',title='rol',obj=rol)

@show.route('usuario/<int:id>')
@login_required
def s_usuario(id):
    usuario = get_usuario_by_id(id)
    user = list(usuario.__dict__.items())
    user.pop(0)
    user.sort(reverse=True)
    user.pop(1)
    return render_template('showBase.html',title='usuario',obj=user)