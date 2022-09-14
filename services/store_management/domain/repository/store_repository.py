"""
Store Repository Interface
"""
from abc import abstractmethod
from typing import Tuple

from core.types import Failure
from ..entities.store import Store


class StoreRepository:
    async def init(self):
        pass

    @abstractmethod
    async def get_store_by_id(self, id) -> Tuple[Store, Failure]:
        raise NotImplementedError()

    @abstractmethod
    async def get_list_store(self) -> Tuple[list, None]:
        raise NotImplementedError()
