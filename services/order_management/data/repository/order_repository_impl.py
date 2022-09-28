from typing import Tuple
from core.types.failure import Failure
from ...domain.repository.order_repository import OrderRepository
from ..dao.order_dao import OrderDao
from ...domain.entities.order import Order
from services.order_management.domain.entities import order


class OrderRepositoryImpl(OrderRepository):
    def __init__(self) -> None:
        super().__init__()
        self.order_dao = OrderDao()

    async def init(self):
        from core.modules.sql_module import create_database_tables
        await create_database_tables()

    async def get_order_by_id(self, order_id) -> Tuple[Order, Failure]:
        order = await self.order_dao.find_one_or_none(id = order_id)
        print('order', order)
        if order is not None:
            return order, None
        return None, Failure(401, "No order")

    async def update_pickup_time(self, order_id, take_time_from, take_time_to) -> Tuple[Order, Failure]:
        order = await self.order_dao.find_one(id=order_id)
        print(order)
        if order is not None:
            order = self.order_dao.merge(order, take_time_from=take_time_from, take_time_to=take_time_to)
            print(order.take_time_from)
            await self.order_dao.save(order)
            return order, None
        return None, Failure(401, "Can not set pickup time.")

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
