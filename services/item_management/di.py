from kink import di

from .data.repository import ItemRepositoryImpl
from .domain.repository import ItemRepository


async def init_di():
    repository = ItemRepositoryImpl()
    await repository.init()

    di[ItemRepository] = repository
