from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from . import crud, schemas
from sqlalchemy.orm import Session
from .database import SessionLocal, engine

origins= ["*"]

# fruits = ["apple","orange","papaya","banana"]
# fruits_detail = {
#     "apple" : {
#         "amount" : 12,
#         "price" : 24,
#     },
#     "orange" : {
#         "amount" : 63,
#         "price" : 61,
#     },"papaya" : {
#         "amount" : 11,
#         "price" : 27,
#     },
#     "banana" : {
#         "amount" : 15,
#         "price" : 2,
#     },
# }
# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: int
#     tax: float | None = None

# class Fruit(BaseModel):
#     name:str
#     amount:int
#     price:float

# class FruitUpdate(BaseModel):
#     amount: int
#     price: float

app = FastAPI()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/db/fruit")
async def get_fruit(db: Session = Depends(get_db)):
    fruits = crud.get_fruit(db=db)
    return fruits

@app.get("/db/fruit/{fruit_id}")
def get_fruit_by_id(fruit_id: int, db: Session = Depends(get_db)):
    fruit = crud.get_fruit_by_id(db, fruit_id=fruit_id)
    if fruit is None:
        raise HTTPException(status_code=404, detail="Fruit not found")
    return fruit


# @app.put("/items/{item_id}")
# async def create_item(item_id: int, item: Item, q: str | None = None):
#     result = {"item_id": item_id, **item.dict()}
#     if q:
#         result.update({"q": q})
#     return result

# @app.get("/fruit")
# async def get_fruit(limit:int = 0):
#     if limit == 0:
#         return fruits
#     return fruits[0:limit]

# @app.get("/fruit/{fruit_name}")
# async def get_fruit_detail(fruit_name):
#     return fruits_detail[fruit_name]

# @app.post("/fruit")
# async def add_fruit(new_fruit:Fruit):
#     fruits.append(new_fruit.name)
#     fruits_detail[new_fruit.name] = {
#         "amount": new_fruit.amount,
#         "price" : new_fruit.price 
#     }
#     return f"add {new_fruit.name} completed"

# @app.put("/fruit/{fruit_name}")
# async def update_fruit(fruit_name: str, fruit_update: FruitUpdate):
#     if fruit_name in fruits_detail:
#         fruits_detail[fruit_name]["amount"] = fruit_update.amount
#         fruits_detail[fruit_name]["price"] = fruit_update.price
#         return fruits_detail[fruit_name]
#     else:
#         return {"error": f"Fruit {fruit_name} not found"}
    
# @app.delete("/fruit/{fruit_name}")
# async def delete_fruit(fruit_name: str):
#     if fruit_name in fruits:
#         fruits.remove(fruit_name)
#         return {"message": f"Fruit {fruit_name} deleted successfully"}
#     else:
#         return {"error": f"Fruit {fruit_name} not found"}




