from ..dao import StoreDAO
from ...domain.repository import StoreRepository
from .address_repository_impl import AddressRepositoryImpl


class StoreRepositoryImpl(StoreRepository):
    def __init__(self) -> None:
        super().__init__()
        self.store_dao = StoreDAO()
        self.address_repository_impl = AddressRepositoryImpl()

    async def init(self):
        from core.modules.sql_module import create_database_tables
        await create_database_tables()

    async def get_store_by_id(self, id):
        # Access to db here
        json_data = {
            'store_id': 1,
            'user_id': 10,
            'device_id': 10,
            'device_type': 'ios',
            'address_id': 100,
            'created_at': '21/06/2021',
            'updated_at': '22/06/2022'
        }
        return json_data

    async def get_list_store(self):
        list_store = await self.store_dao.find(None, status="ACTIVE")
        for store in list_store:
            store.id = str(store.id)
            print(store.address_id)
            store.address = await self.address_repository_impl.get_address_by_id(store.address_id)
        return list_store

    # async def get_address_by_id(self, get_store_by_id_usecase: GetAddressUseCase = Depends(GetAddressUseCase)):
    #     pass
