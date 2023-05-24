from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

from DatabaseConnection import DatabaseConnection
from DAO.restaurantDAO import RestaurantDao
from DAO.productDAO import ProductDao

app = FastAPI()

# Define el modelo Restaurant para el esquema de datos.
class Restaurant(BaseModel):
    id: int
    nombre: str
    url: str
    descripcion: str

    class Config:
        orm_mode = True

class Product(BaseModel):
    id: int
    nombre: str
    url: str
    descripcion: str
    tipo: str


@app.get("/restaurants", response_model=List[Restaurant])
async def read_restaurants():
    db_connection = DatabaseConnection('consorcio', 'consorcio', 'nomelase123', '144.24.54.17', '5432')
    restaurant_dao = RestaurantDao(db_connection)
    restaurants = restaurant_dao.get_restaurants()
    return restaurants

@app.get("/products/{restaurant_id}", response_model=List[Restaurant])
async def read_restaurants(restaurant_id: int):
    db_connection = DatabaseConnection('consorcio', 'consorcio', 'nomelase123', '144.24.54.17', '5432')
    product_dao = ProductDao(db_connection)
    products = product_dao.get_products(restaurant_id)
    return products