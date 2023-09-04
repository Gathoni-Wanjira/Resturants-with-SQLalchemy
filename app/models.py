from sqlalchemy import create_engine;
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

engine = create_engine('sqlite:///hospitality.db')


class Restaurant(Base):
    __tablename__ = "restaurants"
    
    id = Column(Integer(), primary_key = True)
    name = Column(String(), index = True)
    price = Column(Integer())
    
    def __repr__(self):
        return f"Resturant name : {self.name}, price: {self.price}"
        
        
class Customer(Base):
    __tablename__ = "customers"
    
    id = Column(Integer(), primary_key = True)
    first_name = Column(String(), index = True)
    last_name = Column(String())
    
    def __repr__(self):
        return f"Customers firstname : {self.first_name}, price: {self.last_name}"
        
    
    
    
    
    