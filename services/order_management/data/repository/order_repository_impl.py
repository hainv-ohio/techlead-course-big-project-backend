from typing import Tuple
from core.types.failure import Failure
from ...domain.repository.order_repository import OrderRepository
from ..models.order_dao import OrderDao
from ...domain.entities.order import Order


class OrderRepositoryImpl(OrderRepository):
    def __init__(self) -> None:
        super().__init__()
            
    async def get_order_by_id(self, order_id: str) -> Tuple[Order, Failure]:
        # Access db to get Order by order Id
        # Example data
        return OrderDao.from_json({
            'order_id': '1',
            'status': 1,
            'customer_id': '1',
            'shop_id': '1',
            'take_time_start': '1',
            'take_time_end': '1'
        })

    async def save(self, order) -> Tuple[bool, Failure]:
        # Save Order to database if save bool return true else return false
        return True

    async def delete(self, order: Order) -> bool:
        # Delete Order if delete successful return true else return false
        pass

    async def delete_by_id(self, order_id: str) -> bool:
        # Delete Order by order_id if delete successful return true else return false
        pass

    async def get_list_order_by_customer_id(self, customer_id: str):
        # Get orders by customer_id
        # return array of Order or empty array
        pass

    async def get_list_order_by_shop_id(self, shop_id: str):
        # Get list orders by shop_id
        # return array of Order or empty array
        pass

    async def send_message_to_user(self, topic, order) -> Tuple[bool, Failure]:
        # self.order_producer.send_message_to_user(topic=topic, value=order)
        pass

    async def receive_message_from_user(self, order) -> Tuple[bool, Failure]:
        pass
