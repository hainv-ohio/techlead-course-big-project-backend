
from .base import BaseOrderUsecase


class GetOrderUsecase(BaseOrderUsecase):
    def __init__(self) -> None:
        super().__init__()

    async def execute(self, order_id):
        order = await self.repository.get_order_by_id(order_id)
        if order:
            self.repository.send_message_to_user(topic="get_order_by_id_action", value=order)
        return {
            'status': 'success',
            'message': '',
            'data': {
                'order_id': order.order_id,
                "status": order.status,
                "customer_id": order.customer_id,
                "shop_id": order.shop_id,
                "take_time_start": order.take_time_start,
                "take_time_end": order.take_time_end
            }
        }
        
