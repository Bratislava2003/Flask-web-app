__all__ = (
    "db",
    "Base"
)

from typing import TYPE_CHECKING
from flask_sqlalchemy import SQLAlchemy, BaseQuery
from sqlalchemy.orm import declared_attr

db = SQLAlchemy()


class Base(db.Model):

    __abstract__ = True

    @declared_attr
    def __tablename__(cls):
        return f'{cls.__name__.lower()}s'

    if TYPE_CHECKING:
        query: "BaseQuery"
