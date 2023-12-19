from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from src.schemas import schema
from src.infra.sqlalchemy.repositories.product import Repo_product
from src.infra.sqlalchemy.config.database import create_db, get_db


create_db()

app = FastAPI()

# cd app-blx\backend & uvicorn server:app --reload

@app.post('/products')
def create_product(product : schema.Product, db : Session = Depends(get_db)):
    created_product = Repo_product(db).create_product(product)
    return created_product

@app.get('/products')
def show_products(db : Session = Depends(get_db)):
    products = Repo_product(db).show_product()
    return products