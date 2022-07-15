from dataclasses import dataclass
from datetime import datetime

@dataclass
class Order:
    order_id: str
    status: str
    customer_id: str
    shop_id: str
    take_time_start: datetime
    take_time_end: datetime