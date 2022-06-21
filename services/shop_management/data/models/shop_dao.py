from datetime import datetime

from ...domain.entities.shop import Shop


class ShopDAO(Shop):
    def __init__(self, shop_id: str, user_id: str, device_id: str, device_type: str, address_id: int,
                 created_at: datetime, updated_at: datetime, *args, **kwargs) -> None:
        super().__init__(shop_id, user_id, device_id, device_type, address_id, created_at, updated_at, *args, **kwargs)

    @staticmethod
    def from_json(json_data) -> Shop:
        return Shop(json_data['shop_id'], json_data['user_id'], json_data['device_id'], json_data['device_type'],
                    json_data['address_id'], json_data['created_at'], json_data['updated_at'])
