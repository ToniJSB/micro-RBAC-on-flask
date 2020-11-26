from flask_login.utils import login_required
from app_flask.app.security.dao import create_permiso, create_rol, create_usuario, get_all_permisos
from flask import Blueprint,url_for,render_template, redirect
from flask.helpers import flash
from .forms import RegisterPermisoForm, RegisterRolForm, RegisterUsuarioForm
from app_flask.app.security.models import db, Permiso, Usuario, Rol
from app_flask.app import bcrypt,manager_login


create = Blueprint('create',__name__)

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