import sys
sys.path.append('/Users/ddanghyni0425/kiosktest/kiosk/domain/order')
from order_schema import Order_
import sys
sys.path.append('/Users/ddanghyni0425/kiosktest/kiosk')
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session, joinedload
from database import get_db
import models
from typing import List


router = APIRouter()

#!  OrderDetail을 사용해서 주문 받는 post 그리고 스키마를 사용해서 데이터를 받는다.
@router.post('/order', tags = ['주문 등록'])
def create_order(request: Order_, db: Session = Depends(get_db)):
    new_order = models.OrderDetail(orderer_id=request.orderer,
                              menu_pk=request.menu, 
                              menu_count=request.count)
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order

