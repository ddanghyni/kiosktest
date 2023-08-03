import sys
sys.path.append('/Users/ddanghyni0425/kiosktest/kiosk/domain/menu')
from menu_schema import MenuCategory
import sys
sys.path.append('/Users/ddanghyni0425/kiosktest/kiosk')
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session, joinedload
from database import get_db
import models
from typing import List


router = APIRouter(
    tags=['메뉴']
)

#! 카테고리 목록 조회
@router.get('/categories')
def 카테고리_목록_조회(db: Session = Depends(get_db)):
    categories = db.query(models.Categories).all()
    return categories



#! category_pk로 메뉴 조회
@router.get('/menu/{category_pk}', response_model=List[MenuCategory])
def 카테고리별_메뉴_조회(category_pk: int, db: Session = Depends(get_db)):
    menus = db.query(models.Menu).options(joinedload(models.Menu.category)).filter(models.Menu.category_pk == category_pk).all()
    return [{"menu_pk": menu.menu_pk, 
             "menu_name": menu.menu_name, 
             "menu_price": menu.menu_price,
             "menu_description": menu.menu_description, 
             "category_name": menu.category.category_name} for menu in menus]

## 
