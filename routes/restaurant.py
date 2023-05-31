from fastapi import APIRouter, HTTPException
from database.database import get_database
from typing import List

restaurant_routes = APIRouter()


@restaurant_routes.get("/restaurants")
async def read_restaurants() -> List[dict]:
    query = "SELECT * FROM restaurant"
    try:
        database = await get_database()
        restaurants = await database.fetch_all(query)
        return [dict(restaurant) for restaurant in restaurants]
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

