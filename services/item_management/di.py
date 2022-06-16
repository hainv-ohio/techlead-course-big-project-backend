
from kink import di
from .domain.repository import ItemRepository
from .data.repository import ItemRepositoryImpl

from .domain.usecases import *

async def init_di():
    repository =  ItemRepositoryImpl()
    await repository.init()

    di[ItemRepository] = repository