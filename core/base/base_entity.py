from datetime import datetime
from typing import Dict
"""
Just control the dependencies of Entities here
"""
class BaseEntity(object):

    def to_json(self, keys=None) -> Dict:
        return {k: v for k, v in self.__dict__.items() if not '__' in k and (keys is None or k in keys)}

"""
Common Entitity with common fields
"""
class CommonEntity(BaseEntity):
    id: str
    created_at: datetime
    created_by: str
    updated_at: datetime
    updated_by: str
    is_deleted: bool
    deleted_at: datetime
    deleted_by: str


class StringDetailEntity(BaseEntity):
    language: str
    name: str
    description: str