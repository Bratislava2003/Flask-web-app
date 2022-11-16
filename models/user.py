from .database import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


class User(Base):
    id = Column(Integer, primary_key=True, unique=True)
    user_name = Column(String, unique=False, nullable=False, default="")
    username = Column(String, unique=True, nullable=False, default="")
    email = Column(String, unique=True, nullable=False, default="")
    posts = relationship("Post", back_populates="user", uselist=True)
