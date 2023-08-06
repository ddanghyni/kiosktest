import sys
sys.path.append('/Users/ddanghyni0425/kiosktest/kiosk')
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session, joinedload
from database import get_db
import models
from typing import List


router = APIRouter(
    tags=['메뉴 추천']
)

def age_to_age_group(age: int) -> int:
   
    if age >= 50:
        return 50
    else:
        return (age // 10) * 10



@router.get('/recommendation/{orderer_id}')
def 고객_메뉴_추천(orderer_id: int, db: Session = Depends(get_db)):
    # 주문자 정보 가져오기
    orderer = db.query(models.Orderer).filter(models.Orderer.orderer_id == orderer_id).first()
    if not orderer:
        raise HTTPException(status_code=404, detail="Orderer not found")

    # 나이를 연령대로 변환
    age_group = age_to_age_group(orderer.orderer_age)

    # 해당 연령대와 성별에 해당하는 추천 메뉴들 찾기
    recommendations = (
        db.query(models.RecommendedMenu)
        .filter(models.RecommendedMenu.age == age_group, models.RecommendedMenu.gender == orderer.orderer_gender)
        .all()
    )

    if not recommendations:
        return {"message": "No recommendations available for this age group and gender."}

    recommended_menus = [
        {
            "menu_name": recommendation.menu.menu_name,
            "menu_description": recommendation.menu.menu_description,
            "menu_price": recommendation.menu.menu_price
        }
        for recommendation in recommendations
    ]

    return {"recommended_menus": recommended_menus}
