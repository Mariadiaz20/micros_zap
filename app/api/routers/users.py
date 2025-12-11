from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from app.db.session import get_db
from app import schemas, crud
from app.models.models import Usuario

router = APIRouter(prefix="/users", tags=["users"])

@router.get("", response_model=List[schemas.UsuarioOut])
def list_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_list(db, Usuario, skip, limit)

@router.get("/{user_id}", response_model=schemas.UsuarioOut)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_item(db, Usuario, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/", response_model=schemas.UsuarioOut)
def create_user(payload: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    return crud.create_item(db, Usuario, payload.dict())

@router.put("/{user_id}", response_model=schemas.UsuarioOut)
def update_user(user_id: int, payload: schemas.UsuarioUpdate, db: Session = Depends(get_db)):
    updated = crud.update_item(db, Usuario, user_id, payload.dict())
    if not updated:
        raise HTTPException(status_code=404, detail="User not found")
    return updated

@router.delete("/{user_id}", response_model=schemas.UsuarioOut)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_item(db, Usuario, user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    return deleted