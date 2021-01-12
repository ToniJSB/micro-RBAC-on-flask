from flask import flash,redirect,render_template,url_for,request
from flask.json import dumps
from flask_login import login_required
from flask_babel import lazy_gettext as _l
from app_flask.app import manager_login, bcrypt
from app_flask.app.database import remove_extra_attr
from app_flask.app.managment.models import Usuario
from app_flask.app.managment.forms import RegisterUsuarioForm, UpdateUsuarioForm
from app_flask.app.managment.usuario.service import *
from app_flask.app.managment.utils import getattrs_from_form, get_languages

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
            to_val = find_usuario_by_username(request.args.get(args))[0]
        else:
            dep = request.args.get(args)
    # Funciona cuando solicitco un delete _ Es para la autorización del borrado

    if sure == 'True':
        return render_template('viewBase.html',obj=usuarios,title='usuario',transTitle=_l('usuario'),sure=sure,dep=dep,to_val=to_val, lang = get_languages())
    
    return render_template('viewBase.html',obj=usuarios,title='usuario',transTitle=_l('usuario'),dep = dep , to_val=to_val, lang = get_languages())

@login_required
def c_usuario():
    """
    Requiere de autentificación
    Fabrica una vista para crear un usuario
    """
    form = RegisterUsuarioForm()
    form_constructor = getattrs_from_form(form)
    if form.validate_on_submit():
        user = create_usuario(form)
        flash(_l('Cuenta creada para ')+ user.username + '!', 'success')
        return redirect(url_for('managment.v_usuario'))

    return render_template('createBase.html', form=form,constructor=form_constructor,title='usuario',lang = get_languages())

@login_required
def u_usuario(id):
    """
    Requiere de autentificación
    Fabrica una vista para modificar el usuario
    pasado por parámetro con su id
    """
    form = UpdateUsuarioForm()
    form_constructor = getattrs_from_form(form)
    
    if form.validate_on_submit():
        modify_usuario(id,form)
        flash(_l('el usuario ha sido modificado'),'success')
        return redirect(url_for('managment.v_usuario'))

    elif request.method == 'GET':
        usuarioG = find_usuario_by_id(id)[0]
        form.username.data = usuarioG.username 
        form.first_name.data = usuarioG.first_name 
        form.last_name.data = usuarioG.last_name
        rolesId = []
        for rol in usuarioG.roles:
            rolesId.append(rol.id)
    
    return render_template('createBase.html', form=form,constructor=form_constructor, ids=rolesId, lang= get_languages())


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
        return redirect(url_for('managment.v_usuario',sure=True,dep='roles', obj=find_usuario_by_id(id)[0]))

    return redirect(url_for('managment.v_usuario'))

@login_required
def s_usuario(id):
    """
    Requiere de autentificación
    Fabrica una vista para mostrar el permiso
    pasado por parámetro con su id
    """
    usuario = find_usuario_by_id(id)[0]
    
    remove_extra_attr(usuario)
    user = list(usuario.__dict__.items())
    user.sort(reverse=True)
    
    return render_template('showBase.html',title='usuario',transTitle=_l('usuario'),obj=user, lang= get_languages())

@login_required
def f_usuario():
    lista = []
    if request.method == 'POST':
        data_filter = dict(request.get_json())
        
        for filter in data_filter.values():
            for usuario in find_usuarios_by(filter['attr'],filter['simil'],filter['text']):
                
                remove_extra_attr(usuario)
                # usuario.__dict__.pop('usuario')

                lista.append(usuario.__dict__)
    usuarios_n = find_all_usuarios(lista)
    
    return dumps(usuarios_n)
