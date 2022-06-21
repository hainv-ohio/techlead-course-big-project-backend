from ..models import ShopDAO
from ...domain.repository import ShopRepository


class ShopRepositoryImpl(ShopRepository):
    def __init__(self) -> None:
        super().__init__()

    async def get_shop_by_id(self, id):
        # Access to db here
        json_data = {
            'shop_id': 1,
            'user_id': 10,
            'device_id': 10,
            'device_type': 'ios',
            'address_id': 100,
            'created_at': '21/06/2021',
            'updated_at': '22/06/2022'
        }
        return ShopDAO.from_json(json_data)
