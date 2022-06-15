from kink import di, inject
from .base import BaseShopUsecase

class GetBaseShopUsecase(BaseShopUsecase):
    def __init__(self) -> None:
        super().__init__()

    async def execute(self, id):
        return await self.repository.get_shop_by_id(id)