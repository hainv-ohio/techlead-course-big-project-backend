"""
Store Repository Interface
"""
from typing import Tuple

from core.types import Failure
from ..entities.store import Store


class StoreRepository:
    async def init(self):
        pass

    async def get_store_by_id(self, id) -> Tuple[Store, Failure]:
        raise NotImplementedError()

    async def receive_message_from_user(self, message) -> None:
        raise NotImplementedError()
