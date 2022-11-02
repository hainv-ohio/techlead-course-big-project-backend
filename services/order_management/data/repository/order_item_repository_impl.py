from typing import Tuple
from core.types import Failure

from ..dao.order_item_dao import OrderItemDAO
from ...domain.repository.order_item_repository import OrderItemRepository
from ..orm.order_item_orm import OrderItemORM
from ...domain.entities.order_item import OrderItem

from kink import inject

@inject
class OrderItemRepositoryImpl(OrderItemRepository):
    # def __init__(self, messaging_module: MessagingModule) -> None:
    def __init__(self) -> None:
        super().__init__()
        self.order_item_dao = OrderItemDAO()

    async def init(self):
        from core.modules.sql_module import create_database_tables
        await create_database_tables()

    async def save(self, order_item: OrderItem):
        order_item = OrderItemORM(**{
            **order_item.to_json(keys=['id', 'order_id', 'item_id', 'qty', 'price'])
        })
        await self.order_item_dao.save(order_item)
        return order_item

