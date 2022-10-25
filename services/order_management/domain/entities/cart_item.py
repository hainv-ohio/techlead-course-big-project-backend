from datetime import datetime
from core.base import CommonEntity
from dataclasses import dataclass

@dataclass
class CartItem(CommonEntity):
    cart_id: str
    item_id: str
    name: str
    category_id: int
    price: float
    currency_code: str
    detail: str
    qty: int
    
