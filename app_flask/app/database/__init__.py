from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



def remove_extra_attr(obj):
    """
    Elimina los atributos del modelo SQLAlchemy que no deseemos
    """
    
    if 'password' in obj.__dict__ :
        obj.__dict__.pop('password')
    obj.__dict__.pop('_sa_instance_state')
    obj.__dict__.pop('created_on')
    obj.__dict__.pop('changed_on')
    obj.__dict__.pop('created_by_fk')
    obj.__dict__.pop('changed_by_fk')
    pass