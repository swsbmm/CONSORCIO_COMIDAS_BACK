from fastapi import FastAPI
from typing import List
from fastapi.middleware.cors import CORSMiddleware
from database.connection import PostgresDatabase
from routes.product import product_routes
from routes.restaurant import restaurant_routes
from database.database import get_database

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

dsn = "postgresql://consorcio:nomelase123@heflox.com:5432/consorcio1"
db = PostgresDatabase(dsn)

@app.on_event("startup")
async def startup_event():
    database = await get_database()
    await database.connect()

@app.on_event("shutdown")
async def shutdown_event():
    database = await get_database()
    await database.disconnect()

app.include_router(product_routes, prefix='/api')
app.include_router(restaurant_routes, prefix='/api')

# @app.get("/restaurants", response_model=List[Restaurant])
# async def read_restaurants():
#     db_connection = DatabaseConnection('consorcio', 'consorcio', 'nomelase123', '144.24.54.17', '5432')
#     restaurant_dao = RestaurantDao(db_connection)
#     restaurants = restaurant_dao.get_restaurants()
#     return restaurants

# @app.get("/products/{restaurant_id}", response_model=List[Product])
# async def read_restaurants(restaurant_id: int):
#     db_connection = DatabaseConnection('consorcio', 'consorcio', 'nomelase123', '144.24.54.17', '5432')
#     product_dao = ProductDao(db_connection)
#     products = product_dao.get_products(restaurant_id)
#     return products