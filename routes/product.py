
from typing import List
from fastapi import APIRouter, File, UploadFile, HTTPException
from database.database import get_database
from starlette.requests import Request
import shutil


product_routes = APIRouter()

@product_routes.get("/products/")
async def read_products() -> List[dict]:
    query = f"SELECT * FROM product"
    try:
        database = await get_database()
        restaurants = await database.fetch_all(query)
        return [dict(restaurant) for restaurant in restaurants]
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@product_routes.get("/products/{restaurant_id}")
async def read_products(restaurant_id: str) -> List[dict]:
    query = f"SELECT * FROM product WHERE id = '{restaurant_id}'"
    try:
        database = await get_database()
        restaurants = await database.fetch_all(query)
        return [dict(restaurant) for restaurant in restaurants]
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@product_routes.post("/product/{product_id}/upload-image")
async def upload_image(request: Request, product_id: str, file: UploadFile = File(...)):
    # Obtener el nombre del archivo
    file_name = file.filename

    # Definir la ubicación para almacenar la imagen
    upload_folder = "./resources/images"
    file_location = f"{upload_folder}/{file_name}"

    # Guardar la imagen en la ubicación especificada
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Actualizar la columna 'image_url' en la base de datos
    database = await get_database()
    product = await database.fetch_one(
        query="SELECT * FROM product WHERE id = :product_id",
        values={"product_id": product_id}
    )

    if product:
        await database.execute(
            query="UPDATE product SET image_url = :image_url WHERE id = :product_id",
            values={"image_url": file_location, "product_id": product_id}
        )

    return {"message": "Image uploaded successfully"}