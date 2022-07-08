from kink import di

from .data.repository.order_repository_impl import OrderRepositoryImpl
from .domain.repository.order_repository import OrderRepository


async def init_di():
    repository = OrderRepositoryImpl()
    await repository.init()

    di[OrderRepository] = repository
