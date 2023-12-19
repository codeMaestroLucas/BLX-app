from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from src.schemas import schema
from src.infra.sqlalchemy.repositories.user import Repo_user
from src.infra.sqlalchemy.repositories.product import Repo_product
from src.infra.sqlalchemy.repositories.order import Repo_order
from src.infra.sqlalchemy.config.database import create_db, get_db


create_db()

app = FastAPI()

# cd app-blx\backend & uvicorn server:app --reload
# cd app-blx\backend & uvicorn server:app --reload --reload-dir=src


################# USERS #################
@app.post('/users')
def create_new_user(user : schema.User, db : Session = Depends(get_db)):
    created_user = Repo_user(db).create_user(user)
    return created_user

@app.get('/users')
def show_all_users(db : Session = Depends(get_db)):
    users = Repo_user(db).show_user()
    return users
#! Isn't working


################# PRODUCTS #################
@app.post('/products')
def create_new_product(product : schema.Product, db : Session = Depends(get_db)):
    created_product = Repo_product(db).create_product(product)
    return created_product

@app.get('/products')
def show_all_products(db : Session = Depends(get_db)):
    products = Repo_product(db).show_product()
    return products


################# ORDERS #################
@app.post('/orders')
def create_new_order(order : schema.Order, db : Session = Depends(get_db)):
    created_order = Repo_order(db).create_order(order)
    return created_order
#! Didn't make it work because need User e Product

@app.get('/orders')
def show_all_orders(db : Session = Depends(get_db)):
    orders = Repo_order(db).show_order()
    return orders