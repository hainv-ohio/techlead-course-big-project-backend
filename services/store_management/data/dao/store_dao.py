
from core.base.base_dao import BaseDao
from ..orm import StoreORM

class StoreDAO(BaseDao):
    model = StoreORM
