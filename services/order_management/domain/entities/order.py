from dataclasses import dataclass
from datetime import datetime
from core.base import CommonEntity

@dataclass
class Order(CommonEntity):
    id: str
    status: int
    customer_id: str
    store_id: str
    take_time_from: datetime
    take_time_to: datetime
    created_at: datetime
    updated_at: datetime
