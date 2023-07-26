import sys
sys.path.append('/Users/ddanghyni0425/kiosktest/kiosk/domain/order')
from order_schema import OrderCreate, OrderResponse
import sys
sys.path.append('/Users/ddanghyni0425/kiosktest/kiosk')
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session, joinedload
from database import get_db
import models
from typing import List


router = APIRouter()

# @router.post("/order/", response_model=OrderResponse)
# def create_order(order: OrderCreate, db: Session = Depends(get_db)):
#     orderer = db.query(models.Orderer).filter(models.Orderer.orderer_id == order.orderer_id).first()
#     if not orderer:
#         raise HTTPException(status_code=404, detail="Orderer not found")
    
#     new_order = models.OrderDetail(
#         orderer_id = order.orderer_id,
#         menu_pk = order.menu_pk,
#         menu_count = order.menu_count
#     )
#     db.add(new_order)
#     db.commit()
#     return new_order
@router.post("/order/", response_model=OrderResponse)
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    orderer = db.query(models.Orderer).filter(models.Orderer.orderer_id == order.orderer_id).first()
    if not orderer:
        raise HTTPException(status_code=404, detail="Orderer not found")
    
    menu = db.query(models.Menu).filter(models.Menu.menu_pk == order.menu_pk).first()
    if not menu:
        raise HTTPException(status_code=404, detail="Menu not found")
    
    new_order = models.OrderDetail(
        orderer_id = order.orderer_id,
        menu_pk = order.menu_pk,
        menu_count = order.menu_count
    )
    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    # calculate total price
    total_price = menu.menu_price * order.menu_count

    # return total price as well
    return {"order_detail_pk": new_order.order_detail_pk, 
            "orderer_id": new_order.orderer_id,
            "menu_pk": new_order.menu_pk,
            "menu_count": new_order.menu_count,
            "menu_price": menu.menu_price,
            "total_price": total_price}