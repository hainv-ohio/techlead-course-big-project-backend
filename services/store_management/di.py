from kink import di

from .data.repository import StoreRepositoryImpl
from .data.repository import AddressRepositoryImpl
from .domain.repository import StoreRepository
from .domain.repository import AddressRepository


# from .domain.usecases import *

async def init_di():
    store_repository = StoreRepositoryImpl()
    address_repository = AddressRepositoryImpl()
    await store_repository.init()
    await address_repository.init()
    print("adsdsdsds")
    di[StoreRepository] = store_repository
    di[AddressRepository] = address_repository
