
from dataclasses import dataclass
from core.base import CommonEntity

@dataclass
class User(CommonEntity):
    first_name: str
    last_name: str
    phone_number: str
    email: str
    is_created: bool = True
    is_verified: bool = False
    profile_image_url: str = ""
    status: str = "ACTIVE"
