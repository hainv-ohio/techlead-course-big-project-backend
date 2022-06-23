from fastapi import Depends
from kink import di, inject

from services.order_management.domain.entities.order import Order
from .base import BaseOrderUsecase
from ..repository.order_repository import OrderRepository

class OrderAction(BaseOrderUsecase):
    def __init__(self, repository: OrderRepository = Depends(OrderRepository), order: Order = Depends(Order)) -> None:
        super().__init__(repository, order)
        
    async def execute(self, order_id):
        order = self.repository.get_order_by_id(order_id)
        order.status = 1
        return self.repository.save(order)
        