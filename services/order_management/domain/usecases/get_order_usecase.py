
from .base import BaseOrderUsecase


class GetOrderUsecase(BaseOrderUsecase):
    def __init__(self) -> None:
        super().__init__()

    async def execute(self, order_id):
        return self.repository.get_order_by_id(order_id)
