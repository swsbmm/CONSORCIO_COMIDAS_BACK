from pydantic import BaseModel

class Product(BaseModel):
    id: int
    nombre: str
    url: str
    descripcion: str
    tipo: str

