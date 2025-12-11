from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models import Usuario, Producto, Pedido  # Assuming these models are defined in models.py

def get_current_user(db: Session = Depends(get_db), user_id: int):
    user = db.query(Usuario).filter(Usuario.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

def get_current_product(db: Session = Depends(get_db), product_id: int):
    product = db.query(Producto).filter(Producto.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

def get_current_order(db: Session = Depends(get_db), order_id: int):
    order = db.query(Pedido).filter(Pedido.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order