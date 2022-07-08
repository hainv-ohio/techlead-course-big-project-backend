from ..models import ItemDAO
from ...domain.repository import ItemRepository
from ..events.item_producer import ItemProducer

class ItemRepositoryImpl(ItemRepository):
    def __init__(self) -> None:
        super().__init__()

    async def get_item_by_id(self, id):
        return ItemDAO.from_json({
            'id': 1,
            'name': 'item_test',
            'category_id': 2,
            'price': '20000',
            'currency_code': 1,
            'detail': 'detail test'
        })

    async def send_item_message(self, item):
        return ItemProducer.send_item_message(item)
