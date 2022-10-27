from kink import di

from .data.repository.order_repository_impl import OrderRepositoryImpl
from .data.repository.cart_repository_impl import CartRepositoryImpl
from .domain.repository.order_repository import OrderRepository
from .domain.repository.cart_repository import CartRepository

async def init_di():
    order_repository = OrderRepositoryImpl()
    cart_repository = CartRepositoryImpl()
    await order_repository.init()
    await cart_repository.init()

    di[OrderRepository] = order_repository
    di[CartRepository] = cart_repository
