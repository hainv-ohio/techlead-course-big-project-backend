from core.base.base_dao import BaseDao
from ..orm.order_orm import OrderORM

class OrderDao(BaseDao):
    model = OrderORM