import sys
sys.path.append('/Users/ddanghyni0425/kiosktest/kiosk/domin/meun')
from meun_schema import Meun

import sys
sys.path.append('/Users/ddanghyni0425/kiosktest/kiosk')
from models import coffee, tea, ade, smoothie, cake
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from typing import List

router = APIRouter(
    prefix="/meun",
    tags=["meun"]
)

@router.get("/list/coffee",response_model=List[Meun])
def get_coffee_list(db: Session = Depends(get_db)):
    coffee_list = db.query(coffee).all()
    return coffee_list

@router.get("/list/tea", response_model=List[Meun])
def get_tea_list(db: Session = Depends(get_db)):
    tea_list = db.query(tea).all()
    return tea_list

@router.get("/list/ade", response_model=List[Meun])
def get_ade_list(db: Session = Depends(get_db)):
    ade_list = db.query(ade).all()
    return ade_list

@router.get("/list/smoothie", response_model=List[Meun])
def get_smoothie_list(db: Session = Depends(get_db)):
    smoothie_list = db.query(smoothie).all()
    return smoothie_list

@router.get("/list/cake", response_model=List[Meun])
def get_cake_list(db: Session = Depends(get_db)):
    cake_list = db.query(cake).all()
    return cake_list
