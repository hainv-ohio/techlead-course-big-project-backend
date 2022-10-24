from dataclasses import dataclass
from core.base import CommonEntity
from .address import Address


@dataclass
class Store(CommonEntity):
    id: str
    name: str
    phone_number: str
    address_id: str
    status: str
    time_open: str
    time_close: str
    address: Address


