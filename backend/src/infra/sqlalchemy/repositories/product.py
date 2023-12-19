from sqlalchemy.orm import Session
from src.schemas import schema
from src.infra.sqlalchemy.models import models


class Repo_product():
    def __init__(self, db : Session):
        self.db = db
        
    def create_product(self, product : schema.Product):
        db_product = models.Product(
            name = product.name,
            details = product.details,
            price = product.price,
            available = product.available
        )
        
        self.db.add(db_product)  # Adding the product on the database
        self.db.commit()  # Confirm the transaction
        self.db.refresh(db_product)  # Grant the consistency of the datas
        return db_product
        
        
    def show_product(self):
          products = self.db.query(models.Product).all()
          return products
          
    def get_by_id(self, product_id : int):
        ...
        
    def remove_product(self, product_id : int):
        ...