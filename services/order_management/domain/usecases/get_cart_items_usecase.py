
from typing import Tuple

from core.types import Failure
from .base import BaseUsecase
from ..entities.order import Order



class GetCartItems(BaseUsecase):
    def __init__(self) -> None:
        super().__init__()

    async def execute(self, cart_id):
        return await self.cart_repository.find_cart_items(ids)
        
        
        
