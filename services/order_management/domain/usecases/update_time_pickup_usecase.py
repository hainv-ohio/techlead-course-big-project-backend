from core.types import failure
from services.order_management.domain.entities import order
from .base import BaseUsecase


class UpdateTimePickupUsecase(BaseUsecase):
    def __init__(self) -> None:
        super().__init__()

    async def execute(self, order_id, take_time_from, take_time_to):
        order, failure = await self.repository.update_pickup_time(order_id, take_time_from, take_time_to)
        return order, failure

