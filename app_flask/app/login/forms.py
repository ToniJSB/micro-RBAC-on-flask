from flask_wtf import FlaskForm
from flask_babel import lazy_gettext as _l
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField(_l('Username'),validators=[DataRequired()])
    password = PasswordField(_l('Password'),validators=[DataRequired()])
    submit = SubmitField(_l('Submit'))

    
