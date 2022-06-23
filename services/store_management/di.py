from kink import di

from .data.repository import StoreRepositoryImpl
from .domain.repository import StoreRepository


# from .domain.usecases import *

async def init_di():
    repository = StoreRepositoryImpl()
    await repository.init()

    di[StoreRepository] = repository
