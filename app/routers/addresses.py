from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from app.db.session import get_db
from app import schemas, crud
from app.models.models import Direccion

router = APIRouter(prefix="/addresses", tags=["addresses"])

@router.get("", response_model=List[schemas.DireccionOut])
def list_addresses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_list(db, Direccion, skip, limit)

@router.get("/{addr_id}", response_model=schemas.DireccionOut)
def get_address(addr_id: int, db: Session = Depends(get_db)):
    addr = crud.get_item(db, Direccion, addr_id)
    if not addr:
        raise HTTPException(status_code=404, detail="Address not found")
    return addr

@router.post("", response_model=schemas.DireccionOut)
def create_address(payload: schemas.DireccionCreate, db: Session = Depends(get_db)):
    return crud.create_item(db, Direccion, payload.dict())

@router.put("/{addr_id}", response_model=schemas.DireccionOut)
def update_address(addr_id: int, payload: schemas.DireccionUpdate, db: Session = Depends(get_db)):
    updated = crud.update_item(db, Direccion, addr_id, payload.dict())
    if not updated:
        raise HTTPException(status_code=404, detail="Address not found")
    return updated

@router.delete("/{addr_id}", response_model=schemas.DireccionOut)
def delete_address(addr_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_item(db, Direccion, addr_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Address not found")
    return deleted