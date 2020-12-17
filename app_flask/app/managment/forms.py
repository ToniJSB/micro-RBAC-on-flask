from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, ValidationError
from wtforms.ext.sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField
from wtforms.fields.core import BooleanField, Field, FieldList, FormField, Label, UnboundField
from wtforms.widgets.core import CheckboxInput, ListWidget, TextInput
from app_flask.app.managment.models import Permiso, Rol, Usuario
from flask_babel import lazy_gettext as _l


class CustomField(QuerySelectField):
    widget = ListWidget()
    option_widget = CheckboxInput()
    
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
    nombre = StringField(_l('Nombre'),validators=[DataRequired()])
    descripcion = StringField(_l('Descripcion'),validators=[DataRequired()])
    
    permisos = CustomField(query_factory=lambda : Permiso.query.all(),
        get_pk= lambda a: a.id,
        get_label= lambda a: a.nombre
    )
    #permiso = FieldList(FormField(PermisosRolForm),default= lambda : Permiso.query.all())
    #permisos = FieldList(StringField('perm',render_kw={'readonly':True}),default= lambda : Permiso.query.all())
    #permiso = QuerySelectField(_l('permisos'),
    #    query_factory= lambda : Permiso.query.all(),
    #    get_pk= lambda a: a.id,
    #    get_label= lambda a: a.nombre,
    #    widget=ListWidget() )
    submit = SubmitField(_l('Enviar'))


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
    username = StringField(_l('Nombre de usuario'),validators=[DataRequired()])
    first_name = StringField(_l('Nombre'), validators=[DataRequired()])
    last_name = StringField(_l('Apellidos'), validators=[DataRequired()])
    password = PasswordField(_l('Contraseña'))
    confirm_password = PasswordField(_l('Confirmar Contraseña'),validators=[ EqualTo('password')])

    roles = QuerySelectMultipleField(_l('roles'),
        query_factory= lambda : Rol.query.all(),
        get_pk=lambda a: a.id,
        get_label=lambda a: a.nombre )

    submit = SubmitField(_l('Enviar'))
    
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

    username = StringField(_l('Nombre de usuario'),validators=[DataRequired()])
    first_name = StringField(_l('Nombre'), validators=[DataRequired()])
    last_name = StringField(_l('Apellidos'), validators=[DataRequired()])
    password = PasswordField(_l('Contraseña'),validators=[DataRequired()])
    confirm_password = PasswordField(_l('Confirmar Contraseña'),validators=[DataRequired(), EqualTo('password')])

    roles = QuerySelectMultipleField(_l('roles'),
        query_factory= lambda : Rol.query.all(),
        get_pk=lambda a: a.id,
        get_label=lambda a: a.nombre )

    submit = SubmitField(_l('Enviar'))

    def validate_username(self,username):
        user = Usuario.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError(_l('Este usuario está en uso. Tendrás el elegir otro'))

