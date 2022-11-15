from .database import Base
from sqlalchemy import Column, Integer, String


class Product(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True, nullable=False)
