from abc import ABC

from ..dao import AddressDAO
from ...domain.repository import AddressRepository
from core.types import Failure


class AddressRepositoryImpl(AddressRepository, ABC):
    def __init__(self) -> None:
        super().__init__()
        self.address_dao = AddressDAO()

    async def init(self):
        from core.modules.sql_module import create_database_tables
        await create_database_tables()

    async def get_address_by_id(self, id):
        address = await self.address_dao.find_one(id=id)
        address.id = str(address.id)
        return address
