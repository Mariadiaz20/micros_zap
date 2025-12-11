from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from app.db.session import get_db
from app import schemas, crud
from app.models.models import PedidoProducto

router = APIRouter(prefix="/order-items", tags=["order-items"])

@router.get("", response_model=List[schemas.OrderItemOut])
def list_order_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_list(db, PedidoProducto, skip, limit)

@router.get("/{item_id}", response_model=schemas.OrderItemOut)
def get_order_item(item_id: int, db: Session = Depends(get_db)):
    it = crud.get_item(db, PedidoProducto, item_id)
    if not it:
        raise HTTPException(status_code=404, detail="Order item not found")
    return it

@router.post("", response_model=schemas.OrderItemOut)
def create_order_item(payload: schemas.OrderItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db, PedidoProducto, payload.dict())

@router.put("/{pedido_id}/{producto_id}", response_model=schemas.OrderItemOut)
def update_order_item(pedido_id: int, producto_id: int, payload: schemas.OrderItemUpdate, db: Session = Depends(get_db)):
    # composite PK: try to fetch by filtering
    obj = db.query(PedidoProducto).filter_by(pedido_id=pedido_id, producto_id=producto_id).first()
    if not obj:
        raise HTTPException(status_code=404, detail="Order item not found")
    updated = crud.update_item(db, type(obj), (pedido_id, producto_id), payload.dict())  # fallback won't work for composite
    # do manual update instead for composite key
    for k, v in payload.dict().items():
        if v is not None:
            setattr(obj, k, v)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

@router.delete("/{pedido_id}/{producto_id}", response_model=schemas.OrderItemOut)
def delete_order_item(pedido_id: int, producto_id: int, db: Session = Depends(get_db)):
    obj = db.query(PedidoProducto).filter_by(pedido_id=pedido_id, producto_id=producto_id).first()
    if not obj:
        raise HTTPException(status_code=404, detail="Order item not found")
    db.delete(obj)
    db.commit()
    return obj