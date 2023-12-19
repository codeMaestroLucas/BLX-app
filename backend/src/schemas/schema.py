from pydantic import BaseModel
from typing import Optional, List

class User(BaseModel):
    id_ : Optional[str] = None
    name : str
    number : str
    # my_sales : List[Order]
    # my_orders : List[Order]
    # my_products : List[Product]
    
    
class Product(BaseModel):
    id_ : Optional[str] = None
    # owner : User
    name : str
    details : Optional[str] = "No details available"
    price : float
    available : bool = False
    
    
    #? Convert a Schema (JSON) to Model (DB)
    class Config():
        orm_mode = True
    
class Order(BaseModel):
    id_ : Optional[str] = None
    user: User
    product : Product
    amount : int
    to_deliver : bool = True
    address : str
    comments : Optional[str] = "No comments."
    
    