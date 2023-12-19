from sqlalchemy import Column, Integer, String, Boolean, Float
from src.infra.sqlalchemy.config.database import Base

class Product(Base):
    __tablename__ = 'product'
    
    id_ = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    details = Column(String)
    price = Column(Float)
    available = Column(Boolean)
    