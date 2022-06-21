from ..models import ItemDAO
from ...domain.repository import ItemRepository


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
