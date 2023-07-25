from pydantic import BaseModel

#! 카테고리 별로 메뉴 조회를 할 때 사용하는 스키마
class MenuCategory(BaseModel):
    menu_pk: int
    menu_name: str
    menu_price: int
    menu_description: str
    category_name: str

    class Config:
        from_attributes = True