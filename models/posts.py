from .database import Base
from sqlalchemy import Column, String, ForeignKey, INTEGER
from sqlalchemy.orm import relationship


class Post(Base):
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    user_id = Column(INTEGER, ForeignKey('users.id'), unique=False, nullable=False)
    title = Column(String, unique=False, nullable=False)
    body = Column(String, unique=False, nullable=False, default="No body detected")
    user = relationship("User", back_populates="posts", uselist=False)
