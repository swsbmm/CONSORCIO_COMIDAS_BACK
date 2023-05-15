from fastapi import FastAPI

consorcio_api = FastAPI()

@consorcio_api.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@consorcio_api.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}