from dataclasses import dataclass
from core.base import CommonEntity

@dataclass
class Item(CommonEntity):
    id: str
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
    image: str
