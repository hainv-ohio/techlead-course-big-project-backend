from datetime import datetime
from os import stat
from xmlrpc.client import boolean


class Order:
    def __init__(self,
                 order_id: str,
                 status: int,
                 customer_id: str,
                 shop_id: str,
                 take_time_start: datetime,
                 take_time_end: datetime,
                 *args, **kwargs) -> None:
        self.order_id = order_id
        self.status = status
        self.customer_id = customer_id
        self.shop_id = shop_id
        self.take_time_start = take_time_start
        self.take_time_end = take_time_end
    