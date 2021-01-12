from getpass import getpass
import click
from flask.cli import with_appcontext
from app_flask.app import current_app,bcrypt
from app_flask.app.database import db
from app_flask.app.managment.models import Permiso, Rol, Usuario

@click.command(name='database')
@with_appcontext
def create_db():
    db.create_all()


@click.command(name='admin')
@with_appcontext
def create_admin():
    username = input('username: ')
    first_name = input('first name: ')
    last_name = input('last name: ')
    password = getpass('password: ')
    confirm_password = getpass('confirm password: ')

    if password == confirm_password:
        hashed_pass = bcrypt.generate_password_hash(password).decode('utf-8')
        user = Usuario(username=username,first_name=first_name,last_name=last_name,password=hashed_pass)
        
        ownId = db.engine.execute('select max(id) from usuario')
        laid = [row[0] for row in ownId]
        
        if laid[0] == None:
            laid[0] = 0

        user.created_by_fk = laid[0] + 1
        user.changed_by_fk = laid[0] + 1
        db.session.add(user)
        db.session.commit()
