
from dataclasses import dataclass
from core.base import CommonEntity

@dataclass
class Store(CommonEntity):
    id: str
    name: str
    phone_number: str
    address_id: str
    status: str
