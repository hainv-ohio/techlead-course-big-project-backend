
from typing import Tuple

from core.types import Failure
from .base import BaseUsecase
from ..entities.cart import Cart



class GetCartIdByCustomerIdUsecase(BaseUsecase):
    def __init__(self) -> None:
        super().__init__()

    async def execute(self, customer_id):
        cart = await self.cart_repository.get_cart_by_customer_id(customer_id=customer_id) 
        return cart
        
        
        
