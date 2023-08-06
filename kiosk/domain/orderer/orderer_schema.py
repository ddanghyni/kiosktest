from pydantic import BaseModel

class Orderer_(BaseModel):
    name: str
    phone: str
    gender: str
    age: int

    class Config():
        from_attributes = True