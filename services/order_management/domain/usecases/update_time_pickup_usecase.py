from .base import BaseUsecase


class UpdateTimePickupUsecase(BaseUsecase):
    def __init__(self) -> None:
        super().__init__()

    async def execute(self, order_id, datetime_pickup):
        order, get_order_failure = await self.repository.get_order_by_id(order_id=order_id)
        if get_order_failure:
            return get_order_failure

        order_dict = order.dict()
        order_dict['start_date'] = datetime_pickup
        result, save_failure = await self.repository.save(order=order_dict)
        if save_failure:
            return save_failure
        return result

