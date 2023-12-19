from sqlalchemy.orm import Session
from src.schemas import schema
from src.infra.sqlalchemy.models import models

class Repo_user():
    def __init__(self, db : Session):
        self.db = db
        
    def create_user(self, user : schema.User):
        db_user = models.User(
            name = user.name,
            number = user.number
        )
        return db_user
    
    def show_user(self):
        users = self.db.query(models.User).all()
        return users
    