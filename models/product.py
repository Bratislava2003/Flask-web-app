from .database import Base
from sqlalchemy import Column, Integer, String


class Product(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True, nullable=False)
    prod_type = Column(String(15), unique=False, nullable=False)
    description = Column(String(300), unique=False, nullable=False, default="No description yet ")
