from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_db():
    from app_flask.app.managment.models import Permiso, Rol, Usuario
    db.create_all()

def remove_extra_attr(obj):
    if 'password' in obj.__dict__ :
        obj.__dict__.pop('password')
    obj.__dict__.pop('_sa_instance_state')
    obj.__dict__.pop('created_on')
    obj.__dict__.pop('changed_on')
    obj.__dict__.pop('created_by_fk')
    obj.__dict__.pop('changed_by_fk')
    pass