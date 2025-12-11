from typing import Any, List, Optional

def create_order(db: Any, order_data: dict) -> dict:
    """Stub: crear orden."""
    return {"id": 1, **(order_data or {})}

def get_order(db: Any, order_id: int) -> Optional[dict]:
    """Stub: obtener orden."""
    return {"id": order_id, "status": "pending"}

def get_orders(db: Any) -> List[dict]:
    """Stub: listar órdenes."""
    return []

def create_producto(db: Any, product_data: dict) -> dict:
    return {"id": 1, **(product_data or {})}

def update_producto(db: Any, product_id: int, product_data: dict) -> Optional[dict]:
    return {"id": product_id, **(product_data or {})}

def get_producto(db: Any, product_id: int) -> Optional[dict]:
    return {"id": product_id, "name": "demo-product"}

def get_productos(db: Any) -> List[dict]:
    return []