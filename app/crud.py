from typing import Type, Any, Dict
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound

def get_list(db: Session, model: Type, skip: int = 0, limit: int = 100):
    return db.query(model).offset(skip).limit(limit).all()

def get_item(db: Session, model: Type, item_id: int):
    return db.query(model).get(item_id)

def create_item(db: Session, model: Type, obj_in: Dict[str, Any]):
    obj = model(**obj_in)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def update_item(db: Session, model: Type, item_id: int, obj_in: Dict[str, Any]):
    obj = get_item(db, model, item_id)
    if not obj:
        return None
    for k, v in obj_in.items():
        if v is not None:
            setattr(obj, k, v)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def delete_item(db: Session, model: Type, item_id: int):
    obj = get_item(db, model, item_id)
    if not obj:
        return None
    db.delete(obj)
    db.commit()
    return obj