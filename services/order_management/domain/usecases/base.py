from kink import di, inject
from ..repository.order_repository import OrderRepository
from ..repository.cart_repository import CartRepository


@inject
class BaseUsecase:
    def __init__(self,
                 repository: OrderRepository,
                 cart_repository: CartRepository) -> None:
        self.repository = repository
        self.cart_repository = cart_repository
