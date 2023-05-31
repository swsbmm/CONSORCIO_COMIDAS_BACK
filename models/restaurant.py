from pydantic import BaseModel

class Restaurant(BaseModel):
    id: int
    nombre: str
    speciality: str
    image_url: str

    class Config:
        orm_mode = True