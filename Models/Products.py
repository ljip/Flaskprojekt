
from sqlalchemy import Column, Integer, String, REAL
from sqlalchemy.ext.declarative import declarative_base

class Product(declarative_base()):
    __tablename__ = "Products"
    ProductID = Column(Integer,primary_key = True, autoincrement=True)
    Name = Column(String, nullable=False)
    Price = Column(Integer, nullable=False)
    