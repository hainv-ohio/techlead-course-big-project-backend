from kink import di

from .data.repository.order_repository_impl import OrderRepositoryImpl
from .domain.repository.order_repository import OrderRepository

async def init_di():
    order_repository = OrderRepositoryImpl()
    await order_repository.init()

    di[OrderRepository] = order_repository
