
from typing import Tuple

from core.types import Failure
from .base import BaseUsecase
from ..entities.order import Order



class GetOrderUsecase(BaseUsecase):
    def __init__(self) -> None:
        super().__init__()

    async def execute(self, order_id) -> Tuple[Order, Failure]:
        print('order_id hi: ', order_id)
        order, failure = await self.repository.get_order_by_id(order_id) 
        return order, failure
        
        
        
