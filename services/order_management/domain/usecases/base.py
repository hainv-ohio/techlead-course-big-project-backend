from kink import di, inject
from ..repository.order_repository import OrderRepository
from ..repository.cart_repository import CartRepository
from ..repository.order_item_repository import OrderItemRepository


@inject
class BaseUsecase:
    def __init__(self,
                 repository: OrderRepository,
                 cart_repository: CartRepository,
                 order_item_repository: OrderItemRepository) -> None:
        self.repository = repository
        self.cart_repository = cart_repository
        self.order_item_repository = order_item_repository
