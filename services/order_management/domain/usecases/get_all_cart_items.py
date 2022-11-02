
from typing import List, Tuple

from core.types import Failure, failure
from .base import BaseUsecase



class GetAllCartItems(BaseUsecase):
    def __init__(self) -> None:
        super().__init__()

    async def execute(self, cart_id):
        cart_items = await self.cart_repository.get_all_cart_items(cart_id=cart_id)
        return cart_items
        
        
        
