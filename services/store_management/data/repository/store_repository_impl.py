from re import A
from typing import Tuple
from core.types import Failure
from ..dao import StoreDAO
from ...domain.repository import StoreRepository
from ...domain.entities.store import Store
from ..orm import StoreORM
from pprint import pprint
import asyncio


class StoreRepositoryImpl(StoreRepository):
    def __init__(self) -> None:
        super().__init__()
        self.store_dao = StoreDAO()

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
        list_store = await self.store_dao.all()
        # pprint(list_store)
        # if list_store is not None:
        #     pprint(list_store)
            # return list_store, None
        return [
                { "value": '1', "label": 'Store 1' },
                { "value": '2', "label": 'Store 2' },
                { "value": '3', "label": 'Store 3' },
                { "value": '4', "label": 'Store 4' },
                { "value": '5', "label": 'Store 5' },
            ]
