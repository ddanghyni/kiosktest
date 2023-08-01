import sys
sys.path.append('/Users/ddanghyni0425/kiosktest/kiosk/domain/order')
from order_schema import OrderCreate, OrderResponse, OrderSummary, Option
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
        "options": [{"option_name": option.option_name, "option_price": option.option_price} for option in selected_options],
        "price": total_price
    }





#! 고객 id에 따른 주문 내역 조회
# @router.get("/order/{orderer_id}",tags=['메뉴 주문 내역 조회'] ,response_model=OrderSummary)
# def read_order(orderer_id: int, db: Session = Depends(get_db)):
#     orderer = db.query(models.Orderer).filter(models.Orderer.orderer_id == orderer_id).first()
#     if not orderer:
#         raise HTTPException(status_code=404, detail="Orderer not found")

#     orders = db.query(models.OrderDetail).options(joinedload(models.OrderDetail.menu)).filter(models.OrderDetail.orderer_id == orderer_id).all()
#     if not orders:
#         raise HTTPException(status_code=404, detail="Order not found")

#     response = []
#     total_price = 0
#     total_count = 0
#     for order in orders:
#         menu_price = order.menu.menu_price
#         price = menu_price * order.menu_count
#         total_price += price
#         total_count += order.menu_count
#         order_info = OrderResponse(
#             orderer_id = order.orderer_id,
#             menu_pk = order.menu_pk,
#             menu_name = order.menu.menu_name,
#             menu_count = order.menu_count,
#             menu_price = menu_price,
#             price = price
#         )
#         response.append(order_info)

#     return {"orderer_name": orderer.orderer_name,"orders": response, "total_count": total_count, "total_price": total_price}

@router.get("/order/{orderer_id}",tags=['메뉴 주문 내역 조회'] ,response_model=OrderSummary)
def read_order(orderer_id: int, db: Session = Depends(get_db)):
    orderer = db.query(models.Orderer).filter(models.Orderer.orderer_id == orderer_id).first()
    if not orderer:
        raise HTTPException(status_code=404, detail="Orderer not found")

    orders = db.query(models.OrderDetail).options(joinedload(models.OrderDetail.menu)).filter(models.OrderDetail.orderer_id == orderer_id).all()
    if not orders:
        raise HTTPException(status_code=404, detail="Order not found")

    total_menu_count = len(orders)  # calculate total menu count

    response = []
    total_price = 0
    for order in orders:
        menu_price = order.menu.menu_price
        price = menu_price
        total_price += price

        options = []
        for option in order.options:
            options.append(Option(option_name=option.option_name, option_price=option.option_price))

        order_info = OrderResponse(
            orderer_id = order.orderer_id,
            menu_pk = order.menu_pk,
            menu_name = order.menu.menu_name,
            menu_price = menu_price,
            price = price,
            options = options
        )
        response.append(order_info)

    return {"orderer_name": orderer.orderer_name, "orders": response, "total_price": total_price, "total_menu_count": total_menu_count}



