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
    
    
    
    
    