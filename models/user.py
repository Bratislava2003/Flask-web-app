from .database import Base
from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.orm import relationship
from flask_login import UserMixin


class User(Base, UserMixin):
    id = Column(Integer, primary_key=True, unique=True)
    username = Column(String, unique=True, nullable=False, default="")
    email = Column(String, unique=True, nullable=False, default="")
    pwd = Column(String, unique=False, nullable=False)
    is_Admin = Column(Boolean(), default=False, nullable=True)
    is_banned = Column(Boolean(), default=False, nullable=True)
    posts = relationship("Post", back_populates="user", uselist=True)
