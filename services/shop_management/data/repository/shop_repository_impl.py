from ...domain.repository import ShopRepository
from ...domain.entities import shop
# from ..models import UserDAO

from core.types import Failure


class ShopRepositoryImpl(ShopRepository):
    def __init__(self) -> None:
        super().__init__()

    async def get_user_by_id(self, id):
        # Access to db here
        return {
            'name': "Haha",
            'phone': '123456'
        }
