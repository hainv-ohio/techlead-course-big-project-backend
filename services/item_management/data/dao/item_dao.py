from core.base.base_dao import BaseDao
from ..orm import ItemORM


class ItemDAO(BaseDao):
    model = ItemORM
