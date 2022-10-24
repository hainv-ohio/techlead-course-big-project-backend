from core.base.base_dao import BaseDao
from ..orm import AddressORM


class AddressDAO(BaseDao):
    model = AddressORM
