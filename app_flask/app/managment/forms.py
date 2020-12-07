from flask_wtf import FlaskForm
from app_flask.app.managment.models import Permiso, Rol, Usuario
from wtforms import StringField, PasswordField, SubmitField
from wtforms.ext.sqlalchemy.fields import QuerySelectMultipleField
from wtforms.validators import DataRequired, EqualTo, ValidationError


class RegisterPermisoForm(FlaskForm):
    nombre = StringField('nombre',validators=[DataRequired()])
    descripcion = StringField('descripcion',validators=[DataRequired()])
    submit = SubmitField('Submit')
    


class RegisterRolForm(FlaskForm):
    nombre = StringField('nombre',validators=[DataRequired()])
    descripcion = StringField('descripcion',validators=[DataRequired()])
    permisos = QuerySelectMultipleField('permisos',
        query_factory= lambda : Permiso.query.all(),
        get_pk= lambda a: a.id,
        get_label= lambda a: a.nombre )
    submit = SubmitField('Submit')


class UpdateUsuarioForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired()])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    password = PasswordField('Password')
    confirm_password = PasswordField('Confirm Password',validators=[ EqualTo('password')])

    roles = QuerySelectMultipleField('roles',
        query_factory= lambda : Rol.query.all(),
        get_pk=lambda a: a.id,
        get_label=lambda a: a.nombre )

    submit = SubmitField('Submit')
    
class RegisterUsuarioForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired()])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(), EqualTo('password')])

    roles = QuerySelectMultipleField('roles',
        query_factory= lambda : Rol.query.all(),
        get_pk=lambda a: a.id,
        get_label=lambda a: a.nombre )

    submit = SubmitField('Submit')

    def validate_username(self,username):
        user = Usuario.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('this username is taken. You must choose a different one')

