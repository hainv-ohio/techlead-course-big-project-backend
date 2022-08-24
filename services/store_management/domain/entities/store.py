
from dataclasses import dataclass
from core.base import CommonEntity

@dataclass
class Store(CommonEntity):
    name: str
    phone_number: str
    address_id: int
    status: str = "ACTIVE"
