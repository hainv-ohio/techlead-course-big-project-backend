from core.base.base_dao import BaseDao
from ..orm.order_item_orm import OrderItemORM


class OrderItemDAO(BaseDao):
    model = OrderItemORM
