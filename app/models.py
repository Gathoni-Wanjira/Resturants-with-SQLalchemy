from sqlalchemy import create_engine;
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

engine = create_engine('sqlite:///hospitality.db')

restaurant_customer = Table(
    'restaurant_customer',
    Base.metadata,
    Column('customer_id', ForeignKey('customers.id'), primary_key=True),
    Column('restaurant_id', ForeignKey('restaurants.id'), primary_key=True),
    extend_existing=True,
)



class Restaurant(Base):
    __tablename__ = "restaurants"
    
    id = Column(Integer(), primary_key = True)
    name = Column(String(), index = True)
    price = Column(Integer())
    
    def __repr__(self):
        return f"Resturant name : {self.name}, price: {self.price}"
    
    customers = relationship('Customer', secondary= restaurant_customer, back_populates='customers')
        
        
class Customer(Base):
    __tablename__ = "customers"
    
    id = Column(Integer(), primary_key = True)
    first_name = Column(String(), index = True)
    last_name = Column(String())
    
    def __repr__(self):
        return f"Customers firstname : {self.first_name}, price: {self.last_name}"
    
    restaurants = relationship('Restaurant', secondary= restaurant_customer, back_populates='restaurants')
        
    
class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer(), primary_key = True)
    star_ratings= Column(Integer())
    
    
    restaurant_id = Column(Integer(), ForeignKey('restaurants.id'))
    customer_id = Column(Integer(), ForeignKey('customers.id'))