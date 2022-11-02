from abc import abstractmethod
from typing import Tuple
from core.types.failure import Failure
from ..entities.order_item import OrderItem


class OrderItemRepository:

    @abstractmethod
    async def init(self):
        raise NotImplementedError()

    @abstractmethod
    async def save(self, order_item):
        raise NotImplementedError()       