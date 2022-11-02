from kink import di

from .data.repository.order_repository_impl import OrderRepositoryImpl
from .data.repository.cart_repository_impl import CartRepositoryImpl
from .data.repository.order_item_repository_impl import OrderItemRepositoryImpl
from .domain.repository.order_repository import OrderRepository
from .domain.repository.cart_repository import CartRepository
from .domain.repository.order_item_repository import OrderItemRepository

async def init_di():
    order_repository = OrderRepositoryImpl()
    cart_repository = CartRepositoryImpl()
    order_item_repository = OrderItemRepositoryImpl()
    await order_repository.init()
    await cart_repository.init()
    await order_item_repository.init()

    di[OrderRepository] = order_repository
    di[CartRepository] = cart_repository
    di[OrderItemRepository] = order_item_repository
