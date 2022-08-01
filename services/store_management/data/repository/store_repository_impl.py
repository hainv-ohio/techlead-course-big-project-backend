from core.types import Failure
from ..models import StoreDAO
from ...domain.repository import StoreRepository


class StoreRepositoryImpl(StoreRepository):
    def __init__(self) -> None:
        super().__init__()

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
        return StoreDAO.from_json(json_data)

    async def receive_message_from_user(self, message):
        print(message)

    async def get_list_store_by_area(self, area_id):
        list_store = {}
        allow_areas = {29, 59, 30, 50}
        if not type(area_id) is int:
            return Failure(500, "Area id must is integer")

        if area_id in allow_areas:
            list_store = {
                'store 1',
                'store 2',
                'store 3'
            }
        return list_store

    async def get_revenue_by_day(self, start_date=None, end_date=None):
        pass
