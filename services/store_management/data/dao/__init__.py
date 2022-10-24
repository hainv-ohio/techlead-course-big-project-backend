from core.base.base_dao import BaseDao
from ..orm.store_orm import StoreORM
from ..orm.address_orm import AddressORM


class StoreDAO(BaseDao):
    model = StoreORM


class AddressDAO(BaseDao):
    model = AddressORM
