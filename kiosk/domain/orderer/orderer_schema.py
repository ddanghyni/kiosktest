from pydantic import BaseModel

class Orderer_(BaseModel):
    name: str
    phone: str

    class Config():
        class Config:
            from_attributes = True