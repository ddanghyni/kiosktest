from pydantic import BaseModel

class Order_(BaseModel):
    orderer:int
    menu:int
    count:int
    
    class Config():
        class Config:
            from_attributes = True