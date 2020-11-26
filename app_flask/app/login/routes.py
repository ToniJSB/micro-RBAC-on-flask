
from flask import Blueprint,url_for,render_template, redirect, g
from flask.globals import request
from flask_login import login_user, login_required
from flask.helpers import flash
from .forms import LoginForm
from app_flask.app.security.models import Usuario
from app_flask.app import bcrypt

auth = Blueprint('auth',__name__)

@auth.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.is_submitted():
        user = Usuario.query.filter_by(username=form.username.data).first()
        print(user)
        if user and bcrypt.check_password_hash(user.password, form.password.data):

            login_user(user)
            g.user = user
            flash('usted está autorizado','success')
            next = request.args.get('next')
            if next:

                return redirect(next)
            else:
                return redirect(url_for('main.home'))

        else:
            flash('usted no está autorizado','warn')
            return redirect(url_for('auth.login'))
    return render_template('login.html',form=form)
