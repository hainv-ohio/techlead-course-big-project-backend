from datetime import datetime
from typing import Tuple
from core.types import Failure

from ...domain.entities.order import Order


class OrderDao(Order):
    def __init__(self, order_id: str, status: int, customer_id: str, shop_id: str, take_time_end: datetime,
                 take_time_start: datetime, *args, **kwargs) -> None:
        super().__init__(order_id, status, customer_id, shop_id, take_time_end, take_time_start, *args, **kwargs)

    @staticmethod
    def from_json(json_data) -> Tuple[Order, Failure]:
        return Order(json_data['order_id'], json_data['status'], json_data['customer_id'], json_data['shop_id'],
                     json_data['shop_id'], json_data['take_time_end'], json_data['take_time_start'])
