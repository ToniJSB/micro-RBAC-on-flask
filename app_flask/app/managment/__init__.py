"""Instancia un Blueprint para encapsular el CRUD del modelo """
from flask import Blueprint
from app_flask.app.managment.permiso.controller import c_permiso, u_permiso, d_permiso, v_permiso, s_permiso, f_permiso
from app_flask.app.managment.rol.controller import c_rol, u_rol, d_rol, v_rol, s_rol, f_rol
from app_flask.app.managment.usuario.controller import c_usuario, u_usuario,d_usuario,v_usuario,s_usuario

managment = Blueprint('managment', __name__)
managment.add_url_rule('/permiso/create',view_func=c_permiso, methods=['GET','POST'])
managment.add_url_rule('/rol/create',view_func=c_rol, methods=['GET','POST'])
managment.add_url_rule('/usuario/create',view_func=c_usuario, methods=['GET','POST'])

managment.add_url_rule('/permiso/update/<int:id>',view_func=u_permiso, methods=['GET','POST'])
managment.add_url_rule('/rol/update/<int:id>',view_func=u_rol, methods=['GET','POST'])
managment.add_url_rule('/usuario/update/<int:id>',view_func=u_usuario, methods=['GET','POST'])

managment.add_url_rule('/permiso/delete/<int:id>/<auth>',view_func=d_permiso, methods=['GET'])
managment.add_url_rule('/rol/delete/<int:id>/<auth>',view_func=d_rol, methods=['GET'])
managment.add_url_rule('/usuario/delete/<int:id>/<auth>',view_func=d_usuario, methods=['GET'])

managment.add_url_rule('/permiso/view',view_func=v_permiso, methods=['GET','POST'])
managment.add_url_rule('/rol/view',view_func=v_rol, methods=['GET','POST'])
managment.add_url_rule('/usuario/view',view_func=v_usuario, methods=['GET','POST'])

managment.add_url_rule('/permiso/show/<int:id>',view_func=s_permiso, methods=['GET'])
managment.add_url_rule('/rol/show/<int:id>',view_func=s_rol, methods=['GET'])
managment.add_url_rule('/usuario/show/<int:id>',view_func=s_usuario, methods=['GET'])

managment.add_url_rule('/permiso/view/filtered',view_func=f_permiso, methods=['GET','POST'])
managment.add_url_rule('/rol/view/filtered',view_func=f_rol, methods=['GET','POST'])