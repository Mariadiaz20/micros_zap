from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from app.db.session import get_db
from app import schemas, crud
from app.models.models import Producto

router = APIRouter(prefix="/products", tags=["products"])

@router.get("", response_model=List[schemas.ProductoOut])
def list_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_list(db, Producto, skip, limit)

@router.get("/{prod_id}", response_model=schemas.ProductoOut)
def get_product(prod_id: int, db: Session = Depends(get_db)):
    p = crud.get_item(db, Producto, prod_id)
    if not p:
        raise HTTPException(status_code=404, detail="Product not found")
    return p

@router.post("/", response_model=schemas.ProductoOut)
def create_product(payload: schemas.ProductoCreate, db: Session = Depends(get_db)):
    return crud.create_item(db, Producto, payload.dict())

@router.put("/{prod_id}", response_model=schemas.ProductoOut)
def update_product(prod_id: int, payload: schemas.ProductoUpdate, db: Session = Depends(get_db)):
    updated = crud.update_item(db, Producto, prod_id, payload.dict())
    if not updated:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated

@router.delete("/{prod_id}", response_model=schemas.ProductoOut)
def delete_product(prod_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_item(db, Producto, prod_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Product not found")
    return deleted