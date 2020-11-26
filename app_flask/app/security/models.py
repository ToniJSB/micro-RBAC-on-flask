from app_flask.app.security.mixin import AuditMixin
from app_flask.app import manager_login
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin


db = SQLAlchemy()

@manager_login.user_loader
def load_user(user_id):
    return Usuario.query.get(user_id)

class Permiso(db.Model, AuditMixin):
    __tablename__ = 'permiso'
    id = db.Column(db.Integer, db.Sequence('permiso_id_seq'), primary_key=True)
    nombre = db.Column(db.String(100), unique=True,nullable=False)
    descripcion = db.Column(db.String(256), nullable=True)

    def __repr__(self):
        return u"{0}, {1}".format(self.id,self.nombre)


assoc_premiso_rol = db.Table(
    'permiso_rol',
    db.Model.metadata,
    db.Column('id', db.Integer, db.Sequence('permiso_rol_id_seq'), primary_key=True),
    db.Column('permiso_id', db.Integer, db.ForeignKey('permiso.id')),
    db.Column('rol_id', db.Integer, db.ForeignKey('rol.id')),
    db.UniqueConstraint('permiso_id', 'rol_id')
)

class Rol(db.Model, AuditMixin):
    __tablename__ =  'rol'

    id = db.Column(db.Integer, db.Sequence('rol_id_seq'), primary_key=True)
    nombre = db.Column(db.String(50), unique= True, nullable=False)
    descripcion = db.Column(db.String(256), nullable=True)
    permisos = db.relationship(
        'Permiso', secondary= assoc_premiso_rol, backref=db.backref('rol',lazy=True)
    )
    def __repr__(self):
        return self.nombre

assoc_usuario_rol = db.Table(
    'usuario_rol',
    db.Model.metadata,
    db.Column('id',db.Integer,db.Sequence('usuario_rol_id_seq'), primary_key=True),
    db.Column('usuario_id',db.Integer, db.ForeignKey('usuario.id')),
    db.Column('rol_id',db.Integer, db.ForeignKey('rol.id')),
    db.UniqueConstraint('usuario_id', 'rol_id')
)

class Usuario(db.Model, UserMixin, AuditMixin):
    __tablename__ = 'usuario'

    id = db.Column(db.Integer, db.Sequence('usuario_id_seq'), primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    first_name = db.Column(db.String(120), nullable=False)
    last_name = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(256), nullable=False)
    roles = db.relationship('Rol',secondary=assoc_usuario_rol,backref=db.backref('usuario',lazy=True))

    def get_id(self):
        return self.id

    def get_full_name(self):
        return u"{0} {1}".format(self.first_name, self.last_name)

    def __repr__(self):
        return self.username