from pydantic import BaseModel
class OrderCreate(BaseModel):
    orderer_id: int
    menu_pk: int
    menu_count: int

    class Config():
        from_atrributes = True

class OrderResponse(BaseModel):
    order_detail_pk: int
    orderer_id: int
    menu_pk: int
    menu_count: int
    menu_price: int
    total_price: int

    class Config():
        from_atrributes = True
