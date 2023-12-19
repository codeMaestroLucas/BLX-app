from sqlalchemy import Column, Integer, String, Boolean, Float
from src.infra.sqlalchemy.config.database import Base
    
class User(Base):
    __tablename__ = 'users'
    
    id_ = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    number = Column(String)

class Product(Base):
    __tablename__ = 'products'
    
    id_ = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    details = Column(String)
    price = Column(Float)
    available = Column(Boolean)
    
class Order(Base):
    __tablename__ = 'orders'
    
    id_ = Column(Integer, primary_key=True, index=True)
    # user = Column() maybe a foreign key
    # product = Column(ForeignKey
    amount = Column(Integer)
    to_deliver = Column(Boolean)
    address = Column(String)
    comments = Column(String)
    