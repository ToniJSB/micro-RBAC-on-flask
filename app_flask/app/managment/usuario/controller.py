from flask import flash,redirect,render_template,url_for,request
from flask_login import login_required
from flask_babel import lazy_gettext as _l
from app_flask.app import manager_login, bcrypt
from app_flask.app.database import remove_extra_attr
from app_flask.app.managment.models import Usuario
from app_flask.app.managment.forms import RegisterUsuarioForm, UpdateUsuarioForm
from app_flask.app.managment.usuario.service import *
from app_flask.app.managment.utils import getattrs_from_form

@login_required
def v_usuario():
    """
    Requiere de autentificación
    Fabrica una vista para ver los usuarios.
    """
    usuarios = find_all_usuarios()

    sure = False
    dep = ''
    to_val = ''
    for args in list(request.args.keys()):
        if args == 'sure':
            sure = request.args.get(args)
        elif args == 'obj':
            to_val = find_usuario_by_username(request.args.get(args))
        else:
            dep = request.args.get(args)
    # Funciona cuando solicitco un delete _ Es para la autorización del borrado

    if sure == 'True':
        return render_template('viewBase.html',obj=usuarios,title='usuario',transTitle=_l('usuario'),sure=sure,dep=dep,to_val=to_val)
    
    return render_template('viewBase.html',obj=usuarios,title='usuario',transTitle=_l('usuario'),dep = dep , to_val=to_val)

@login_required
def c_usuario():
    """
    Requiere de autentificación
    Fabrica una vista para crear un usuario
    """
    form = RegisterUsuarioForm()
    form_constructor = getattrs_from_form(form)

    if form.validate_on_submit():
        print(form.__dict__.get('roles'))
        user = create_usuario(form)
        flash(_l('Cuenta creada para ')+ user.username + '!', 'success')
        return redirect(url_for('managment.v_usuario'))

    return render_template('createBase.html', form=form,constructor=form_constructor,title='usuario')

@login_required
def u_usuario(id):
    """
    Requiere de autentificación
    Fabrica una vista para modificar el usuario
    pasado por parámetro con su id
    """
    form = UpdateUsuarioForm()
    form_constructor = getattrs_from_form(form)
    usuarioG = get_usuario_by_id(id)
    
    if form.validate_on_submit():
        usuarioG.username = form.username.data
        usuarioG.first_name = form.first_name.data
        usuarioG.last_name = form.last_name.data
        usuarioG.roles = form.roles.data
        if form.password.data != '' and form.confirm_password.data != '' and form.confirm_password.data == form.password.data :
            usuarioG.password = bcrypt.generate_password_hash(form.password.data)
        update_usuario()
        flash(_l('el usuario ha sido modificado'),'success')
        return redirect(url_for('managment.v_usuario'))

    elif request.method == 'GET':
        form.username.data = usuarioG.username 
        form.first_name.data = usuarioG.first_name 
        form.last_name.data = usuarioG.last_name
        form.roles.data = usuarioG.roles
    
    return render_template('createBase.html', form=form,constructor=form_constructor)


@login_required
def d_usuario(id,auth):
    """
    Requiere de autentificación
    Hace una primera peticion para solicitar
    la confirmación del borrado
    Al confirmar el borrado elimina el objeto
    """
    
    if auth == 'True':
        confirm_delete_usuario(id)

    elif auth_delete_usuario(id):
        return redirect(url_for('managment.v_usuario',sure=True,dep='roles', obj=get_usuario_by_id(id)))

    return redirect(url_for('managment.v_usuario'))

@login_required
def s_usuario(id):
    """
    Requiere de autentificación
    Fabrica una vista para mostrar el permiso
    pasado por parámetro con su id
    """
    usuario = get_usuario_by_id(id)
    print(usuario.roles)
    remove_extra_attr(usuario)
    user = list(usuario.__dict__.items())
    user.sort(reverse=True)
    
    return render_template('showBase.html',title='usuario',transTitle=_l('usuario'),obj=user)