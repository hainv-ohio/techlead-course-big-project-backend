from datetime import datetime
from core.base import CommonEntity


class Order:
    order_id: str
    status: int
    customer_id: str
    shop_id: str
    take_time_start: datetime
    take_time_end: datetime
    created_at: datetime
    updated_at: datetime
