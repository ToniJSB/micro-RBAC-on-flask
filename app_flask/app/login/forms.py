from flask_wtf import FlaskForm
from flask_babel import lazy_gettext as _l
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField(_l('Nombre de usuario'),validators=[DataRequired()])
    password = PasswordField(_l('Contraseña'),validators=[DataRequired()])
    submit = SubmitField(_l('Enviar'))

    
