from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from app.db.session import get_db
from app import schemas, crud
from app.models.models import Pedido

router = APIRouter(prefix="/orders", tags=["orders"])

@router.get("", response_model=List[schemas.OrderOut])
def list_orders(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_list(db, Pedido, skip, limit)

@router.get("/{order_id}", response_model=schemas.OrderOut)
def get_order(order_id: int, db: Session = Depends(get_db)):
    o = crud.get_item(db, Pedido, order_id)
    if not o:
        raise HTTPException(status_code=404, detail="Order not found")
    return o

@router.post("/", response_model=schemas.OrderOut)
def create_order(payload: schemas.OrderCreate, db: Session = Depends(get_db)):
    return crud.create_item(db, Pedido, payload.dict())

@router.put("/{order_id}", response_model=schemas.OrderOut)
def update_order(order_id: int, payload: schemas.OrderUpdate, db: Session = Depends(get_db)):
    updated = crud.update_item(db, Pedido, order_id, payload.dict())
    if not updated:
        raise HTTPException(status_code=404, detail="Order not found")
    return updated

@router.delete("/{order_id}", response_model=schemas.OrderOut)
def delete_order(order_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_item(db, Pedido, order_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Order not found")
    return deleted