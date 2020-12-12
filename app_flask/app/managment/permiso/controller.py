from flask import flash, redirect, render_template, url_for,request
from flask.json import dumps
from flask_login import login_required
from flask_babel import lazy_gettext as _l
from app_flask.app.database import remove_extra_attr
from app_flask.app.managment.permiso.service import *
from app_flask.app.managment.forms import RegisterPermisoForm
from app_flask.app.managment.utils import getattrs_from_form

@login_required
def v_permiso():
    """
    Requiere de autentificación
    Fabrica una vista para ver los permisos.
    """
    permisos_n = find_all_permisos()    
    permiso =''
    if request.get_json() != None:
        if request.method == 'POST':
            permisos_n =[]
            json_from_req = dict(request.get_json())
            for filter in json_from_req.values():
                for permiso in find_permisos_by(filter['attr'],filter['simil'],filter['text']):
                    
                    remove_extra_attr(permiso)
                    permisos_n.append(permiso)
    else:    
        permiso=permisos_n[0]
        
        remove_extra_attr(permiso)   
        permiso.buttons = ''    
    attr = list(permiso.__dict__.keys())
    print(attr)

    if len(permisos_n)==0:
        return redirect(url_for('managment.c_permiso'))
    
    sure = False
    dep = ''
    to_val = ''
    for args in list(request.args.keys()):
        if args == 'sure':
            sure = request.args.get(args)
        elif args == 'obj':
            to_val = find_permisos_by('nombre','equal',request.args.get(args))
        else:
            dep = request.args.get(args)
    # Funciona cuando solicito un delete _ Es para la autorización del borrado

    if sure == 'True':
        return render_template('viewBase.html',attr=attr,obj=permisos_n,title='permiso', transTitle=_l('Permiso'),sure=sure,dep=dep,to_val=to_val)
    
    return render_template('viewBase.html',attr=attr,obj=permisos_n, title='permiso', transTitle=_l('Permiso'),dep = dep , to_val=to_val)
    

@login_required
def c_permiso():
    """
    Requiere de autentificación
    Fabrica una vista para crear un permiso
    """
    form = RegisterPermisoForm()
    form_constructor = getattrs_from_form(form)

    if form.validate_on_submit():
        permiso = create_permiso(form)
        flash(_l('permiso creado: ')+permiso.nombre+'!', 'success')
        return redirect(url_for('managment.v_permiso'))
    return render_template('createBase.html',form=form,constructor=form_constructor,title='permiso',transTitle=_l('Permiso'))

@login_required
def u_permiso(id):
    """
    Requiere de autentificación
    Fabrica una vista para modificar el permiso
    pasado por parámetro con su id
    """
    form = RegisterPermisoForm()
    form_constructor = getattrs_from_form(form)

    if form.validate_on_submit():
        update_permiso(id, form)
        flash(_l('el permiso ha sido modificado'),'success')
        return redirect(url_for('managment.v_permiso'))

    elif request.method == 'GET':
        permisoG = get_permiso_by_id(id)
        form.nombre.data = permisoG.nombre 
        form.descripcion.data = permisoG.descripcion 
    # Al hacer la primera petición coge los atributos del 
    # objeto a modificar y los introduce en el formulario
    return render_template('createBase.html', form=form,constructor=form_constructor)

@login_required
def d_permiso(id,auth):
    """
    Requiere de autentificación
    Hace una primera peticion para solicitar
    la confirmación del borrado
    Al confirmar el borrado elimina el objeto
    """

    if auth == 'True':
        confirm_delete_permiso(id)

    elif auth_delete_permiso(id):
        return redirect(url_for('managment.v_permiso',sure=True,dep=None, obj=find_permisos_by('id','equals',id)))


    return redirect(url_for('managment.v_permiso'))

@login_required
def s_permiso(id):
    """
    Requiere de autentificación
    Fabrica una vista para mostrar el permiso
    pasado por parámetro con su id
    """
    permiso = get_permiso_by_id(id)
    remove_extra_attr(permiso)
    perm = list(permiso.__dict__.items())
    perm.sort(reverse=True)
    return render_template('showBase.html',title='permiso',transTitle=_l('Permiso'),obj=perm)

@login_required
def f_permiso():
    permisos_n = []
    
    if request.method == 'POST':
        data_filter = dict(request.get_json())
        for filter in data_filter.values():
            for permiso in find_permisos_by(filter['attr'],filter['simil'],filter['text']):
                remove_extra_attr(permiso)
                print(permiso.__dict__)

                permisos_n.append(permiso.__dict__)

    print(dumps(permisos_n))
    return dumps(permisos_n)

