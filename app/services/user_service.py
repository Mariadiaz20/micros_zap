from typing import Any, List, Optional

def create_user(db: Any, user_data: dict) -> dict:
    return {"id": 1, **(user_data or {})}

def update_user(db: Any, user_id: int, user_data: dict) -> Optional[dict]:
    return {"id": user_id, **(user_data or {})}

def get_user(db: Any, user_id: int) -> Optional[dict]:
    return {"id": user_id, "username": "demo-user"}

def get_users(db: Any) -> List[dict]:
    return []
from typing import Any, List, Optional

def create_producto(db: Any, product_data: dict) -> dict:
    return {"id": 1, **(product_data or {})}

def update_producto(db: Any, product_id: int, product_data: dict) -> Optional[dict]:
    return {"id": product_id, **(product_data or {})}

def get_producto(db: Any, product_id: int) -> Optional[dict]:
    return {"id": product_id, "name": "demo-product"}

def get_productos(db: Any) -> List[dict]:
    return []