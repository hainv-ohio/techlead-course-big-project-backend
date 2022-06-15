
from kink import di
from .domain.repository import ShopRepository
from .data.repository import ShopRepositoryImpl

# from .domain.usecases import *

async def init_di():
    repository =  ShopRepositoryImpl()
    await repository.init()

    di[ShopRepository] = repository