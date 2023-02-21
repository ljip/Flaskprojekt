from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

class Employee(declarative_base()):
    __tablename__ = "Employees"
    EmployeeID = Column(Integer,primary_key = True, autoincrement=True)
    Name = Column(String, nullable=False)
    Address = Column(String)
                    
    