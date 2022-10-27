from dataclasses import dataclass
from core.base import CommonEntity


@dataclass
class Address(CommonEntity):
    id: str
    name: str
    map_name: str
    lat: str
    long: str
    country: str
    city: str
    district: str
    ward: str
    detail: str

