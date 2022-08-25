"""
Order repository
"""

from typing import Tuple
from core.types.failure import Failure
from ..entities.order import Order


class OrderRepository:

    async def get_order_by_id(self, order_id: str) -> Tuple[Order, Failure]:
        raise NotImplementedError()

    async def save(self, order) -> Tuple[bool, Failure]:
        raise NotImplementedError()

    async def delete(self, order: Order) -> bool:
        raise NotImplementedError()

    async def delete_by_id(self, order_id: str) -> bool:
        raise NotImplementedError()

    async def get_list_order_by_customer_id(self, customer_id: str):
        raise NotImplementedError()

    async def get_list_order_by_shop_id(self, shop_id: str):
        raise NotImplementedError()
    
    async def init(self):
        pass

    async def send_message_to_user(self, topic, value) -> Tuple[bool, Failure]:
        raise NotImplementedError()

    async def receive_message_from_user(self, user) -> Tuple[bool, Failure]:
        raise NotImplementedError()
