import sys
sys.path.append('/Users/ddanghyni0425/kiosktest/kiosk/domin/meun')
from meun_schema import Meun

import sys
sys.path.append('/Users/ddanghyni0425/kiosktest/kiosk')
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
import models
from typing import List

router = APIRouter(
    prefix="/meun",
    tags=["meun"]
)

@router.get("/list/{menu_type}", response_model=List[Meun])
def get_menu_list(menu_type: str, db: Session = Depends(get_db)):
    menu_model = getattr(models, menu_type, None)
    if menu_model is None:
        raise HTTPException(status_code=400, detail="Invalid menu type")
    menu_list = db.query(menu_model).all()
    return menu_list
