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


router = APIRouter()


#! 고객 정보 조회
@router.get('/orderer', tags = ['고객 정보 조회'])
def get_orderer(db: Session = Depends(get_db)):
    orderer = db.query(models.Orderer).all()
    return orderer

#! 고객 정보 등록 orderer_schema.py에 있는 Orderer를 사용
@router.post('/orderer', tags = ['고객 정보 등록'])
def create_orderer(request: Orderer_, db: Session = Depends(get_db)):
    new_orderer = models.Orderer(orderer_name=request.name, 
                                 orderer_phone=request.phone)  # 수정된 부분
    db.add(new_orderer)
    db.commit()
    db.refresh(new_orderer)
    return new_orderer

