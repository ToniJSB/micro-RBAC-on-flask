from app_flask.app.managment.permiso.service import *
from app_flask.app.database import remove_extra_attr
from app_flask.app.managment.forms import RegisterPermisoForm
from app_flask.app.managment.utils import getattrs_from_form
from flask_login import login_required
from flask import flash, redirect, render_template, url_for,request

@login_required
def v_permiso():
    permisos_n = find_all_permisos()    
    if len(permisos_n)==0:
        return redirect(url_for('managment.c_permiso'))
    sure = False
    dep = ''
    to_val = ''
    for args in list(request.args.keys()):

        if args == 'sure':
            sure = request.args.get(args)
        elif args == 'obj':
            to_val = find_permiso_by_nombre(request.args.get(args))
        else:
            dep = request.args.get(args)

    permiso=permisos_n[0]
    remove_extra_attr(permiso)    
    permiso.buttons = ''    
    attr = list(permiso.__dict__.keys())
    if sure == 'True':
        return render_template('viewBase.html',attr=attr,obj=permisos_n,title='permiso',sure=sure,dep=dep,to_val=to_val)
    
    return render_template('viewBase.html',attr=attr,obj=permisos_n, title='permiso',dep = dep , to_val=to_val)
    

@login_required
def c_permiso():
    form = RegisterPermisoForm()
    form_constructor = getattrs_from_form(form)

    if form.validate_on_submit():
        permiso = create_permiso(form)
        flash('permiso creado: '+permiso.nombre+'!', 'success')
        return redirect(url_for('managment.v_permiso'))
    return render_template('createBase.html',form=form,constructor=form_constructor,title='permiso')

@login_required
def u_permiso(id):
    form = RegisterPermisoForm()
    if form.validate_on_submit():
        update_permiso(id, form)
        flash('el permiso ha sido modificado','success')
        return redirect(url_for('managment.v_permiso'))

    elif request.method == 'GET':
        permisoG = get_permiso_by_id(id)
        form.nombre.data = permisoG.nombre 
        form.descripcion.data = permisoG.descripcion 
    
    return render_template('registerPermiso.html', form=form)

@login_required
def d_permiso(id,auth):

    if auth == 'True':
        confirm_delete_permiso(id)

    elif auth_delete_permiso(id):
        return redirect(url_for('managment.v_permiso',sure=True,dep=None, obj=find_permiso_by_id(id)))


    return redirect(url_for('managment.v_permiso'))

@login_required
def s_permiso(id):
    permiso = get_permiso_by_id(id)
    remove_extra_attr(permiso)
    perm = list(permiso.__dict__.items())
    perm.sort(reverse=True)
    return render_template('showBase.html',title='permiso',obj=perm)
