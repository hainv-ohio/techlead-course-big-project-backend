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
