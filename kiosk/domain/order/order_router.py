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


router = APIRouter()

#! 주문자의 id를 함수값으로 받아서 주문을 하는 라우터
@router.post("/order/{id}", tags=['메뉴 주문'], response_model=OrderResponse)
def create_order(id: int, order: OrderCreate, db: Session = Depends(get_db)):
    # Check if the user with the given id exists
    orderer = db.query(models.Orderer).filter(models.Orderer.orderer_id == id).first()
    if not orderer:
        raise HTTPException(status_code=404, detail="Orderer not found")
    
    menu = db.query(models.Menu).filter(models.Menu.menu_pk == order.menu_pk).first()
    if not menu:
        raise HTTPException(status_code=404, detail="Menu not found")

    # total price starts from the menu price
    total_price = menu.menu_price

    # check if options exist and calculate total price
    selected_options = []
    for option_pk in order.options:
        option = db.query(models.Option).filter(models.Option.option_pk == option_pk).first()
        if not option:
            raise HTTPException(status_code=404, detail=f"Option with pk={option_pk} not found")
        selected_options.append(option)
        total_price += option.option_price

    new_order = models.OrderDetail(
        orderer_id = id,  # Use the id from the path parameter
        menu_pk = order.menu_pk,
    )
    new_order.options = selected_options  # 이 줄을 추가하였습니다.
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


#! 주문자 id를 받아서 주문 내역을 조회하는 라우터

@router.get("/order_check/{orderer_id}", tags=['메뉴 주문 내역 조회'])
def read_orders(orderer_id: int, db: Session = Depends(get_db)):
    # 주문자 정보 조회
    orderer = db.query(models.Orderer).filter(models.Orderer.orderer_id == orderer_id).first()
    if not orderer:
        raise HTTPException(status_code=404, detail="Orderer not found")

    # 주문 정보 조회
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

        options = db.query(models.Option).filter(models.Option.order_details.any(order_detail_pk=order.order_detail_pk)).all()
        options_list = [{"option_name": option.option_name, "option_price": option.option_price} for option in options]

        order_price = menu.menu_price + sum(option.option_price for option in options)

        # 주문 요약 정보 생성
        order_summary = OrderSummary(
            orderer_id=order.orderer_id,
            menu_pk=menu.menu_pk,
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





