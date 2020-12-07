import datetime
from flask_login import current_user
from sqlalchemy import Column, DateTime, ForeignKey, Integer
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import relationship

class AuditMixin(object):
    """
        AuditMixin
        Mixin for models, adds 4 columns to stamp,
        time and user on creation and modification
        will create the following columns:

        :created on:
        :changed on:
        :created by:
        :changed by:
    """

    created_on = Column(DateTime, default=datetime.datetime.now, nullable=False)
    changed_on = Column(
        DateTime,
        default=datetime.datetime.now,
        onupdate=datetime.datetime.now,
        nullable=False,
    )

    @declared_attr
    def created_by_fk(self):
        return Column(
            Integer, ForeignKey("usuario.id"), default=self.get_user_id, nullable=False
        )

    @declared_attr
    def created_by(self):
        return relationship(
            "Usuario",
            primaryjoin="%s.created_by_fk == Usuario.id" % self.__name__,
            enable_typechecks=False,
        )

    @declared_attr
    def changed_by_fk(self):
        return Column(
            Integer,
            ForeignKey("usuario.id"),
            default=self.get_user_id,
            onupdate=self.get_user_id,
            nullable=False,
        )

    @declared_attr
    def changed_by(self):
        return relationship(
            "Usuario",
            primaryjoin="%s.changed_by_fk == Usuario.id" % self.__name__,
            enable_typechecks=False,
        )

    @classmethod
    def get_user_id(self):
        try:
            return current_user.id
        except Exception:
            return None
