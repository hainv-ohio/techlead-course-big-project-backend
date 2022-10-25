"""
Order repository
"""
from abc import abstractmethod
from typing import Tuple
from core.types.failure import Failure
from ..entities.order import Order


class OrderRepository:

    @abstractmethod
    async def get_order_by_id(self, order_id: str) -> Tuple[Order, Failure]:
        raise NotImplementedError()

    @abstractmethod
    async def save(self, order) -> Tuple[bool, Failure]:
        raise NotImplementedError()

    @abstractmethod
    async def delete(self, order: Order) -> bool:
        raise NotImplementedError()

    @abstractmethod
    async def delete_by_id(self, order_id: str) -> bool:
        raise NotImplementedError()

    @abstractmethod
    async def get_list_order_by_customer_id(self, customer_id: str):
        raise NotImplementedError()

    @abstractmethod
    async def get_list_order_by_shop_id(self, shop_id: str):
        raise NotImplementedError()

    @abstractmethod
    async def init(self):
        pass

    @abstractmethod
    async def send_message_to_user(self, topic, value) -> Tuple[bool, Failure]:
        raise NotImplementedError()

    @abstractmethod
    async def receive_message_from_user(self, user) -> Tuple[bool, Failure]:
        raise NotImplementedError()
