"""
Item Repository Interface
"""
from typing import Tuple
from xmlrpc.client import Boolean

from core.types import Failure
from ..entities.item import Item


class ItemRepository:

    async def get_item_by_id(self, id) -> Tuple[Item, Failure]:
        raise NotImplementedError()

    async def get_items_by_category_id(self, id) -> Tuple[list, Failure]:
        raise NotImplementedError()

    async def add_new_item(self, item: Item) -> Tuple[Item, Failure]:
        raise NotImplementedError()

    async def update_item(self, itemUpdate: Item) -> Tuple[Item, Failure]:
        raise NotImplementedError()

    async def update_item_image(self, id, image_path) -> Tuple[Boolean, Failure]:
        raise NotImplementedError()

    async def delete_item(self, id) -> Tuple[Boolean, Failure]:
        raise NotImplementedError()

    async def send_item_message(self, item)-> Tuple[Boolean, Failure]:
         raise NotImplementedError()

    async def init(self):
        pass
