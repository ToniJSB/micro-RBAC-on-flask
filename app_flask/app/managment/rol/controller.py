from sqlalchemy.util.langhelpers import constructor_copy
from app_flask.app.managment.rol.service import *
from app_flask.app.database import remove_extra_attr
from app_flask.app.managment.models import Rol
from app_flask.app.managment.utils import getattrs_from_form
from app_flask.app.managment.forms import RegisterRolForm
from flask_login import login_required
from flask import flash, redirect, render_template, url_for,request


@login_required
def v_rol():
    roles = get_all_roles()
    if len(roles) == 0:
        return redirect(url_for('managment.c_rol'))
    
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

    rol = roles[0]
    remove_extra_attr(rol)
    rol.buttons = ''

    attr=list(rol.__dict__.keys())
    
    if sure == 'True':
        return render_template('viewBase.html',attr=attr,obj=roles,title='rol',sure=sure,dep=dep,to_val=to_val)
    
    return render_template('viewBase.html',attr=attr,obj=roles,title='rol',dep = dep , to_val=to_val)


@login_required
def c_rol():
    form = RegisterRolForm()
    form_constructor = getattrs_from_form(form)
    if form.validate_on_submit():
        print(form.permisos)
        """ rol = Rol(nombre=form.nombre.data,descripcion=form.descripcion.data,permisos=form.permisos.data)"""
        rol = create_rol(form)
        flash('rol created: '+rol.nombre+'!','success')
        return redirect(url_for('managment.v_rol'))
    return render_template('createBase.html', form=form, constructor=form_constructor,title='rol')

@login_required
def u_rol(id):
    form = RegisterRolForm()
    if form.validate_on_submit():
        update_rol(id, form)
        flash('el rol ha sido modificado','success')
        return redirect(url_for('managment.v_rol'))

    elif request.method == 'GET':
        rolG = get_rol_by_id(id)
        form.nombre.data = rolG.nombre 
        form.descripcion.data = rolG.descripcion 
        form.permisos.data = rolG.permisos
    
    return render_template('registerrol.html', form=form)

@login_required
def d_rol(id,auth):
        
    if auth == 'True':
        confirm_delete_rol(id)

    elif auth_delete_rol(id):
        return redirect(url_for('managment.v_rol',sure=True,dep='permisos', obj=find_rol_by_id(id)))

    return redirect(url_for('managment.v_rol'))

@login_required
def s_rol(id):
    role = get_rol_by_id(id)
    remove_extra_attr(role)
    rol = list(role.__dict__.items())
    rol.sort(reverse=True)
    return render_template('showBase.html',title='rol',obj=rol)
