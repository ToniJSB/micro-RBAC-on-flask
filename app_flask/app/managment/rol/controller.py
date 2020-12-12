from flask import flash, redirect, render_template, url_for,request
from flask_login import login_required
from flask_babel import lazy_gettext as _l
from app_flask.app.database import remove_extra_attr
from app_flask.app.managment.models import Rol
from app_flask.app.managment.rol.service import *
from app_flask.app.managment.forms import RegisterRolForm
from app_flask.app.managment.utils import getattrs_from_form


@login_required
def v_rol():
    """
    Requiere de autentificación
    Fabrica una vista para ver los rol.
    """
    roles = get_all_roles()
    if len(roles) == 0:
        return redirect(url_for('managment.c_rol'))
    
    rol = roles[0]
    remove_extra_attr(rol)
    rol.buttons = ''
    attr=list(rol.__dict__.keys())

    sure = False
    dep = ''
    to_val = ''
    for args in list(request.args.keys()):
        if args == 'sure':
            sure = request.args.get(args)
        elif args == 'obj':
            to_val = find_rol_by_nombre(request.args.get(args))
        else:
            dep = request.args.get(args)
    # Funciona cuando solicito un delete _ Es para la autorización del borrado 
    if sure == 'True':
        return render_template('viewBase.html',attr=attr,obj=roles,title='rol',transTitle=_l('rol'),sure=sure,dep=dep,to_val=to_val)
    
    return render_template('viewBase.html',attr=attr,obj=roles,title='rol',transTitle=_l('rol'),dep = dep , to_val=to_val)


@login_required
def c_rol():
    """
    Requiere de autentificación
    Fabrica una vista para crear un rol
    """
    form = RegisterRolForm()
    form_constructor = getattrs_from_form(form)
    if form.validate_on_submit():
        print(form.permisos)
        """ rol = Rol(nombre=form.nombre.data,descripcion=form.descripcion.data,permisos=form.permisos.data)"""
        rol = create_rol(form)
        flash(_l('rol created: ')+rol.nombre+'!','success')
        return redirect(url_for('managment.v_rol'))
    return render_template('createBase.html', form=form, constructor=form_constructor,title='rol',transTitle=_l('rol'))

@login_required
def u_rol(id):
    """
    Requiere de autentificación
    Fabrica una vista para modificar el rol
    pasado por parámetro con su id
    """
    form = RegisterRolForm()
    form_constructor = getattrs_from_form(form)

    if form.validate_on_submit():
        update_rol(id, form)
        flash(_l('el rol ha sido modificado'),'success')
        return redirect(url_for('managment.v_rol'))

    elif request.method == 'GET':
        rolG = get_rol_by_id(id)
        form.nombre.data = rolG.nombre 
        form.descripcion.data = rolG.descripcion 
        form.permisos.data = rolG.permisos
    
    return render_template('createBase.html', form=form, constructor=form_constructor)

@login_required
def d_rol(id,auth):
    """
    Requiere de autentificación
    Hace una primera peticion para solicitar
    la confirmación del borrado
    Al confirmar el borrado elimina el objeto
    """
    
    if auth == 'True':
        confirm_delete_rol(id)

    elif auth_delete_rol(id):
        return redirect(url_for('managment.v_rol',sure=True,dep='permisos', obj=find_rol_by_id(id)))

    return redirect(url_for('managment.v_rol'))

@login_required
def s_rol(id):
    """
    Requiere de autentificación
    Fabrica una vista para mostrar el rol
    pasado por parámetro con su id
    """
    role = get_rol_by_id(id)
    remove_extra_attr(role)
    rol = list(role.__dict__.items())
    rol.sort(reverse=True)
    return render_template('showBase.html',title='rol',transTitle=_l('rol'),obj=rol)
