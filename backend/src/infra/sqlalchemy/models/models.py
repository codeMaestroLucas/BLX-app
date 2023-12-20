from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey
from src.infra.sqlalchemy.config.database import Base
from sqlalchemy.orm import relationship
    
class User(Base):
    __tablename__ = 'users'
    
    id_ = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    number = Column(String)
    
    #### RELATIONS #####
    my_products = relationship('Product', back_populates='my_users')
    #* Every time i call the 'select' on this table i will se the products that related to that user
    
class Product(Base):
    __tablename__ = 'products'
    
    id_ = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    details = Column(String)
    price = Column(Float)
    available = Column(Boolean)
    
    #### RELATIONS #####
    user_id = Column(Integer, ForeignKey('users.id_'))
    my_users = relationship('User', back_populates='my_products')
    
class Order(Base):
    __tablename__ = 'orders'
    
    id_ = Column(Integer, primary_key=True, index=True)
    # user = Column() maybe a foreign key
    # product = Column(ForeignKey
    amount = Column(Integer)
    to_deliver = Column(Boolean)
    address = Column(String)
    comments = Column(String)
    