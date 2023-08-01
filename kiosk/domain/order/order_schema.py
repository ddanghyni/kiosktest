from pydantic import BaseModel
from typing import List


class OrderCreate(BaseModel):
    #orderer_id: int
    menu_pk: int
    menu_count: int
   

    class Config():
        from_attributes = True

class OrderResponse(BaseModel):
    #order_detail_pk: int
    orderer_id: int
    menu_pk: int
    menu_name: str
    menu_count: int
    menu_price: int
    price: int

    
    class Config():
        from_attributes = True

class OrderSummary(BaseModel):
    orderer_name: str
    orders: List[OrderResponse]
    total_count: int
    total_price: int

    class Config():
        from_attributes = True     


