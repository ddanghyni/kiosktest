from pydantic import BaseModel

class Meun(BaseModel):
    id: int
    name: str
    price: int
    description: str

    class Config:
        from_attributes = True