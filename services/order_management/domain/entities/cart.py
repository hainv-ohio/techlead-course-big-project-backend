from dataclasses import dataclass
from datetime import datetime
from core.base import CommonEntity

@dataclass
class Cart(CommonEntity):
    customer_id: str
    status: int
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
