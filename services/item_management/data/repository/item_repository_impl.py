from ..models import ItemDAO
from ...domain.repository import ItemRepository

from core.modules.messaging_module import MessagingModule
from kink import inject

@inject
class ItemRepositoryImpl(ItemRepository):
    def __init__(self, messaging_module: MessagingModule) -> None:
        super().__init__()

        self.messaging_module = messaging_module

    async def get_item_by_id(self, id):
        return ItemDAO.from_json({
            'id': 1,
            'name': 'item_test',
            'category_id': 2,
            'price': '20000',
            'currency_code': 1,
            'detail': 'detail test'
        })
