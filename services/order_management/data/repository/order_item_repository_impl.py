from typing import Tuple
from core.types import Failure
from ...domain.repository.order_item_repository import OrderItemRepository
from ..dao.order_item_dao import OrderItemDAO

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

    async def save(self, order_item):
        orderd_item = self.order_item_dao.save(order_item)
        return orderd_item

