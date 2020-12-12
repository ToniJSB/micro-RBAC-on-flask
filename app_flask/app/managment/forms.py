from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, ValidationError
from wtforms.ext.sqlalchemy.fields import QuerySelectMultipleField
from app_flask.app.managment.models import Permiso, Rol, Usuario
from flask_babel import lazy_gettext as _l


class RegisterPermisoForm(FlaskForm):
    """
        Clase formulario para el registro de los Permisos

        Atributos
        -
        nombre : StringField\n
            Campo requereido para enviar el formulario
        descripcion : StringField\n
            Campo requereido para enviar el formulario
        submit : SubmmitField\n
            Entrega el formulario     
    """
    nombre = StringField(_l('nombre'),validators=[DataRequired()])
    descripcion = StringField(_l('descripcion'),validators=[DataRequired()])
    submit = SubmitField(_l('Submit'))
    


class RegisterRolForm(FlaskForm):
    """
        Clase formulario para el registro de los Roles

        Atributos
        -
        nombre : StringField\n
            Campo requereido para enviar el formulario
        descripcion : StringField\n
            Campo requereido para enviar el formulario
        permisos : [Permiso]\n
            Campo de selección de permisos
        submit : SubmmitField\n
            Entrega el formulario     
    """
    nombre = StringField(_l('nombre'),validators=[DataRequired()])
    descripcion = StringField(_l('descripcion'),validators=[DataRequired()])
    permisos = QuerySelectMultipleField(_l('permisos'),
        query_factory= lambda : Permiso.query.all(),
        get_pk= lambda a: a.id,
        get_label= lambda a: a.nombre )
    submit = SubmitField(_l('Submit'))


class UpdateUsuarioForm(FlaskForm):
    """
        Clase formulario para la Modificación de los Usuarios

        Atributos
        -
        username : StringField\n
            Campo requereido para enviar el formulario
        first_name : StringField\n
            Campo requereido para enviar el formulario
        last_name : StringField\n
            Campo requereido para enviar el formulario
        password : PasswordField\n
            Campo requereido para enviar el formulario
        confirm_password : PasswordField\n
            Campo requereido para enviar el formulario y 
            confirma que sea el mismo texto entre 
            password y confirm password
        roles : [Rol]\n
            Selector de roles
        submit : SubmmitField\n
            Entrega el formulario     
    """
    username = StringField(_l('Username'),validators=[DataRequired()])
    first_name = StringField(_l('First Name'), validators=[DataRequired()])
    last_name = StringField(_l('Last Name'), validators=[DataRequired()])
    password = PasswordField(_l('Password'))
    confirm_password = PasswordField(_l('Confirm Password'),validators=[ EqualTo(_l('password'))])

    roles = QuerySelectMultipleField(_l('roles'),
        query_factory= lambda : Rol.query.all(),
        get_pk=lambda a: a.id,
        get_label=lambda a: a.nombre )

    submit = SubmitField(_l('Submit'))
    
class RegisterUsuarioForm(FlaskForm):
    """
        Clase formulario para la Modificación de los Usuarios

        Atributos
        -
        username : StringField\n
            Campo requereido para enviar el formulario
        first_name : StringField\n
            Campo requereido para enviar el formulario
        last_name : StringField\n
            Campo requereido para enviar el formulario
        password : PasswordField\n
            Campo requereido para enviar el formulario
        confirm_password : PasswordField\n
            Campo requereido para enviar el formulario y 
            confirma que sea el mismo texto entre 
            password y confirm password
        roles : [Rol]\n
            Selector de roles
        submit : SubmmitField\n
            Entrega el formulario
        
        Metodos
        -
        validate_username(username) : Boolean\n
            Método que confirma que el username enviado por el formulario 
            no está en la base de datos
    """

    username = StringField(_l('Username'),validators=[DataRequired()])
    first_name = StringField(_l('First Name'), validators=[DataRequired()])
    last_name = StringField(_l('Last Name'), validators=[DataRequired()])
    password = PasswordField(_l('Password'),validators=[DataRequired()])
    confirm_password = PasswordField(_l('Confirm Password'),validators=[DataRequired(), EqualTo(_l('password'))])

    roles = QuerySelectMultipleField(_l('roles'),
        query_factory= lambda : Rol.query.all(),
        get_pk=lambda a: a.id,
        get_label=lambda a: a.nombre )

    submit = SubmitField(_l('Submit'))

    def validate_username(self,username):
        user = Usuario.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError(_l('this username is taken. You must choose a different one'))

