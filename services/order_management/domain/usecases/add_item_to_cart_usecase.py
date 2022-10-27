
from typing import Tuple

from core.types import Failure, failure
from .base import BaseUsecase
from ..entities.cart import Cart
from ..entities.cart_item import CartItem



class AddItemToCartUsecase(BaseUsecase):
    def __init__(self) -> None:
        super().__init__()

    async def execute(self, item_id, customer_id, qty) -> Tuple[CartItem, Failure]:
        cart_item, failure = await self.cart_repository.add_item_to_cart(item_id=item_id, customer_id=customer_id, qty=qty)
        if cart_item is not None:
            return cart_item, None
        return None, failure
        
        
        
