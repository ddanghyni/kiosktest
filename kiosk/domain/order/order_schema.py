from pydantic import BaseModel
from typing import List


class Option(BaseModel):
    option_name: str
    option_price: int

    class Config():
        from_attributes = True

class OrderCreate(BaseModel):
    menu_pk: int
    options: List[int] = []

    class Config():
        from_attributes = True

class OrderResponse(BaseModel):
    orderer_id: int
    menu_pk: int
    menu_name: str
    menu_price: int
    options: List[Option] = []
    price: int

    class Config():
        from_attributes = True


class OrderSummaryDetail(BaseModel):
    orderer_name: str
    orders: List[OrderResponse]
    total_menu_count: int
    total_price: int

    class Config():
        from_attributes = True




