from dataclasses import dataclass
from core.base import CommonEntity
from .item import Item

@dataclass
class Item(CommonEntity):
    id: int
    name: str
    sku: str
    status: int
    category_id: int
    price: float
    currency_code: int
    sort_description: str
    long_description: str
    total_sale: int
    brand_id: int
