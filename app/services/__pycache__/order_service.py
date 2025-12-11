from typing import Any, List, Optional

def create_order(db: Any, order_data: dict) -> dict:
    return {"id": 1, **(order_data or {})}

def get_order(db: Any, order_id: int) -> Optional[dict]:
    return {"id": order_id, "status": "pending"}

def get_orders(db: Any) -> List[dict]:
    return []