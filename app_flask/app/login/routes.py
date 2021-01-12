from flask import url_for,render_template, redirect, g, session, current_app
from flask.globals import request
from flask_login import login_user
from flask.helpers import flash
from .forms import LoginForm
from app_flask.app.managment.models import Usuario
from app_flask.app.managment.utils import get_languages
from app_flask.app import bcrypt
from flask_babel import lazy_gettext as _l


def login():
    form = LoginForm()


    if form.is_submitted():
        user = Usuario.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data) and user.discharged == None:
            login_user(user)
            g.user = user
            flash(_l('usted está autorizado'),'success')
            return redirect(url_for('main.home'))

        else:
            flash(_l('usted no está autorizado'),'warn')
            return redirect(url_for('auth.login'))
    return render_template('login.html',form=form, lang = get_languages())

def logout():
    session.clear()
    return redirect(url_for('main.home'))