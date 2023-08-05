import sys
sys.path.append('/Users/ddanghyni0425/kiosktest/kiosk/domain/orderer')
from orderer_schema import Orderer_
import sys
sys.path.append('/Users/ddanghyni0425/kiosktest/kiosk')
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session, joinedload
from database import get_db
import models
from typing import List


router = APIRouter(
    tags=['고객 정보']
)


#! 고객 정보 조회
@router.get('/orderer')
def 고객_정보_조회(db: Session = Depends(get_db)):
    orderer = db.query(models.Orderer).all()
    return orderer

#! 고객 정보 등록 
@router.post('/new_orderer')
def 고객_정보_등록(request: Orderer_, db: Session = Depends(get_db)):
    new_orderer = models.Orderer(orderer_name=request.name, 
                                 orderer_phone=request.phone)  # 수정된 부분
    db.add(new_orderer)
    db.commit()
    db.refresh(new_orderer)
    return new_orderer

