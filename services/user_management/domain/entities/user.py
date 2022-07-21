
from dataclasses import dataclass


@dataclass
class User:
    id: str
    full_name: str
    phone_number: str
    email: str
    status: str='ACTIVE'
