from flask import flash, redirect, render_template, url_for,request
from flask.json import dumps
from flask_login import login_required
from flask_babel import lazy_gettext as _l
from app_flask.app.database import remove_extra_attr
from app_flask.app.managment.rol.service import *
from app_flask.app.managment.forms import RegisterRolForm
from app_flask.app.managment.utils import getattrs_from_form


@login_required
def v_rol():
    """
    Requiere de autentificación
    Fabrica una vista para ver los rol.
    """
    roles = find_all_roles()
    if len(roles['lista']) == 0:
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
    # Funciona cuando solicito un delete _ Es para la autorización del borrado 
    if sure == 'True':
        return render_template('viewBase.html',obj=roles,title='rol',transTitle=_l('rol'),sure=sure,dep=dep,to_val=to_val)
    
    return render_template('viewBase.html',obj=roles,title='rol',transTitle=_l('rol'),dep = dep , to_val=to_val)


@login_required
def c_rol():
    """
    Requiere de autentificación
    Fabrica una vista para crear un rol
    """
    form = RegisterRolForm()
    form_constructor = getattrs_from_form(form)

    if form.validate_on_submit():

        rol = create_rol(form)
        flash(_l('rol creado: ')+rol.nombre+'!','success')
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
        modify_rol(id, form)
        flash(_l('el rol ha sido modificado'),'success')
        return redirect(url_for('managment.v_rol'))

    elif request.method == 'GET':
        rolG = find_roles_by('id','equal',id)[0]
        form.nombre.data = rolG.nombre 
        form.descripcion.data = rolG.descripcion 
        permisosid = []
        for perm in rolG.permisos:
            permisosid.append(perm.id)
        
    return render_template('createBase.html', form=form, constructor=form_constructor, ids = permisosid)

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
    role = find_roles_by('id','equal',id)[0]
    role.permisos
    role.__dict__.pop('usuario')
    remove_extra_attr(role)
    rol = list(role.__dict__.items())
    rol.sort(reverse=True)
    return render_template('showBase.html',title='rol',transTitle=_l('rol'),obj=rol)

@login_required
def f_rol():
    roles_n = find_all_roles()
    roles_n['lista'].clear()
    if request.method == 'POST':
        data_filter = dict(request.get_json())
        for filter in data_filter.values():
            print(filter)
            for rol in find_roles_by(filter['attr'],filter['simil'],filter['text']):
                remove_extra_attr(rol)
                rol.__dict__.pop('usuario')
                print(rol.__dict__)

                roles_n['lista'].append(rol.__dict__)

    return dumps(roles_n)
