from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from app.db.session import get_db
from app import schemas, crud
from app.models.models import Categoria

router = APIRouter(prefix="/categories", tags=["categories"])

@router.get("", response_model=List[schemas.CategoriaOut])
def list_categories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_list(db, Categoria, skip, limit)

@router.get("/{cat_id}", response_model=schemas.CategoriaOut)
def get_category(cat_id: int, db: Session = Depends(get_db)):
    cat = crud.get_item(db, Categoria, cat_id)
    if not cat:
        raise HTTPException(status_code=404, detail="Category not found")
    return cat

@router.post("", response_model=schemas.CategoriaOut)
def create_category(payload: schemas.CategoriaCreate, db: Session = Depends(get_db)):
    return crud.create_item(db, Categoria, payload.dict())

@router.put("/{cat_id}", response_model=schemas.CategoriaOut)
def update_category(cat_id: int, payload: schemas.CategoriaUpdate, db: Session = Depends(get_db)):
    updated = crud.update_item(db, Categoria, cat_id, payload.dict())
    if not updated:
        raise HTTPException(status_code=404, detail="Category not found")
    return updated

@router.delete("/{cat_id}", response_model=schemas.CategoriaOut)
def delete_category(cat_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_item(db, Categoria, cat_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Category not found")
    return deleted