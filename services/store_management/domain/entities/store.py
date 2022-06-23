from datetime import datetime


class Store:
    def __init__(self,
                 store_id: str,
                 user_id: str,
                 device_id: str,
                 device_type: str,
                 address_id: int,
                 created_at: datetime,
                 updated_at: datetime,
                 *args, **kwargs) -> None:
        self.store_id = store_id
        self.user_id = user_id
        self.device_id = device_id
        self.device_type = device_type
        self.address_id = address_id
        self.created_at = created_at
        self.updated_at = updated_at
