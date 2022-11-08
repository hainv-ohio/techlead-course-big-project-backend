from typing import Tuple
from core.types import Failure
from ..dao import ItemDAO
from ...domain.entities.item import Item
from ...domain.repository.item_repository import ItemRepository
from ..orm.item_orm import ItemORM

from core.modules.messaging_module import MessagingModule
from kink import inject

@inject
class ItemRepositoryImpl(ItemRepository):
    # def __init__(self, messaging_module: MessagingModule) -> None:
    def __init__(self) -> None:
        super().__init__()
        
        self.item_dao = ItemDAO()
        # self.messaging_module = messaging_module
    async def init(self):
        from core.modules.sql_module import create_database_tables
        await create_database_tables()
        
    async def get_item_by_id(self, id):
        return await self.item_dao.find_one(id=id)

    async def add_new_item(self, item: Item):
        item = ItemORM(**{
            **item.to_json(keys=['name', 'sku', 'status', 'category_id', 'price', 'currency_code', 'sort_description', 'long_description', 'brand_id', 'image']),
        })

    async def get_items_by_ids(self, ids):

        print('-------------------------')
        print(ids)

        items = await self.item_dao.findByIds(ids)
        if items is not None:
            print('--- products ---')
            print(items)
            return items

        return None

    async def get_items_by_category_id(self, id):
        return await self.item_dao.find(None, status=1)

    async def update_item(self, itemUpdate: Item):
        pass

    async def update_item_image(self, id, image_path):
        pass

    async def delete_item(self, id):
        pass

    async def send_item_message(self, item):
        pass
