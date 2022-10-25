"""
Order repository
"""
from abc import abstractmethod
from typing import List, Tuple
from core.types.failure import Failure
from ..entities.cart import Cart
from ..entities.cart_item import CartItem


class CartRepository:
    @abstractmethod
    async def get_cart_by_id(self, order_id: str) -> Tuple[Cart, Failure]:
        raise NotImplementedError()

    @abstractmethod
    async def get_all_cart_item(self, order_id: str) -> Tuple[List[CartItem], Failure]:
        raise NotImplementedError()

    @abstractmethod
    async def add_item_to_cart(self, item_id, customer_id) -> Tuple[CartItem, Failure]:
        raise NotImplementedError()
    