from .database import Base
from .mixins.timemixin import TimestampMixin
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship


class Post(Base, TimestampMixin):
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), unique=False, nullable=False)
    title = Column(String, unique=False, nullable=False)
    body = Column(String, unique=False, nullable=False, default="No body detected")
    category = Column(String(25), nullable=False, default=None)
    user = relationship("User", back_populates="posts", uselist=False)
