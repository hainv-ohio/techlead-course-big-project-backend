
from .base import BaseOrderUsecase


class OrderAction(BaseOrderUsecase):
    def __init__(self) -> None:
        super().__init__()

    async def execute(self, order_id):
        order = self.repository.get_order_by_id(order_id)
        order.status = 1
        return self.repository.save(order)
