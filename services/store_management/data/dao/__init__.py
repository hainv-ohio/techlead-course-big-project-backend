
from core.base.base_dao import BaseDao
from ..orm.store_orm import StoreORM

class StoreDAO(BaseDao):
    model = StoreORM
