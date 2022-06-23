from datetime import datetime

from ...domain.entities.store import Store


class StoreDAO(Store):
    def __init__(self, store_id: str, user_id: str, device_id: str, device_type: str, address_id: int,
                 created_at: datetime, updated_at: datetime, *args, **kwargs) -> None:
        super().__init__(store_id, user_id, device_id, device_type, address_id, created_at, updated_at, *args, **kwargs)

    @staticmethod
    def from_json(json_data) -> Store:
        return Store(json_data['store_id'], json_data['user_id'], json_data['device_id'], json_data['device_type'],
                    json_data['address_id'], json_data['created_at'], json_data['updated_at'])
