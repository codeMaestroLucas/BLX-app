from sqlalchemy.orm import Session
from src.schemas import schema
from src.infra.sqlalchemy.models import models

class Repo_order():
    def __init__(self, db : Session):
        self.db = db
        
    def create_order(self, order : schema.Order):
        db_order = models.Order(
            amount = order.amount,
            to_deliver = order.to_deliver,
            address = order.address,
            comments = order.comments
        )
        return db_order
    
    def show_order(self):
        orders = self.db.query(models.Order).all()
        return orders