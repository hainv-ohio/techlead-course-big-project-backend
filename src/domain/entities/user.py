
from dataclasses import dataclass
from core.base import CommonEntity

@dataclass
class User(CommonEntity):
    first_name: str
    last_name: str
    email: str
