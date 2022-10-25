from dataclasses import dataclass
from datetime import datetime
from core.base import CommonEntity

@dataclass
class OrderItem(CommonEntity):
    id: str
    order_id: str
    product_id: str
    qty: int
    price: float
    
