

"""
User Repository Interface
"""
from typing import List, Tuple
from ..entities.shop import Shop
from core.types import Failure


class ShopRepository:
    async def init(self):
        pass

    async def get_shop_by_id(self, id) -> Tuple[Shop, Failure]:
        raise NotImplementedError()
