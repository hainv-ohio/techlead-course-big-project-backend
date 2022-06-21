"""
User Repository Interface
"""
from typing import Tuple

from core.types import Failure
from ..entities.shop import Shop


class ShopRepository:
    async def init(self):
        pass

    async def get_shop_by_id(self, id) -> Tuple[Shop, Failure]:
        raise NotImplementedError()
