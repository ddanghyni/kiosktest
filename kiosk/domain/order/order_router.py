import sys
sys.path.append('/Users/ddanghyni0425/kiosktest/kiosk/domain/order')
from order_schema import OrderCreate, OrderResponse,OrderSummary
import sys
sys.path.append('/Users/ddanghyni0425/kiosktest/kiosk')
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session, joinedload
from database import get_db
import models
from typing import List


router = APIRouter(
    tags=['주문']
)


@router.post("/order/{id}",response_model=OrderResponse)
def 메뉴_주문(id: int, order: OrderCreate, db: Session = Depends(get_db)):
    orderer = db.query(models.Orderer).filter(models.Orderer.orderer_id == id).first()
    if not orderer:
        raise HTTPException(status_code=404, detail="Orderer not found")
    
    menu = db.query(models.Menu).filter(models.Menu.menu_pk == order.menu_pk).first()
    if not menu:
        raise HTTPException(status_code=404, detail="Menu not found")

    total_price = menu.menu_price

    selected_options = []
    for option_pk in order.options:
        option = db.query(models.Option_).filter(models.Option_.option_pk == option_pk).first()  # 수정
        if not option:
            raise HTTPException(status_code=404, detail=f"Option with pk={option_pk} not found")
        selected_options.append(option)
        total_price += option.option_price

    new_order = models.OrderDetail(
        orderer_id = id,
        menu_pk = order.menu_pk,
    )
    new_order.options = selected_options
    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    return {
        "orderer_id": new_order.orderer_id,
        "menu_pk": new_order.menu_pk,
        "menu_name": menu.menu_name,
        "menu_price": menu.menu_price,
        "price": total_price,
        "options": [{"option_name": option.option_name, "option_price": option.option_price} for option in selected_options]
    }


@router.get("/order_check/{orderer_id}")
def 고객_주문_내역_조회(orderer_id: int, db: Session = Depends(get_db)):
    orderer = db.query(models.Orderer).filter(models.Orderer.orderer_id == orderer_id).first()
    if not orderer:
        raise HTTPException(status_code=404, detail="Orderer not found")

    orders = db.query(models.OrderDetail).filter(models.OrderDetail.orderer_id == orderer_id).all()
    if not orders:
        raise HTTPException(status_code=404, detail="Orders not found")

    response = []
    total_price = 0
    total_menu_count = 0
    for order in orders:
        menu = db.query(models.Menu).filter(models.Menu.menu_pk == order.menu_pk).first()
        if not menu:
            continue

        options = db.query(models.Option_).filter(models.Option_.order_details.any(order_detail_pk=order.order_detail_pk)).all()  # 수정
        options_list = [{"option_name": option.option_name, "option_price": option.option_price} for option in options]

        order_price = menu.menu_price + sum(option.option_price for option in options)

        order_summary = OrderSummary(
            menu_name=menu.menu_name,
            menu_price=menu.menu_price,
            options=options_list,
            total_price=order_price
        )

        total_price += order_price
        total_menu_count += 1
        response.append(order_summary)

    return {
        "orderer_name": orderer.orderer_name,
        "orders": response,
        "total_menu_count": total_menu_count,
        "Final payment amount": total_price
    }





