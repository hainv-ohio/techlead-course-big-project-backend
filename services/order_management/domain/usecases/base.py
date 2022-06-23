<<<<<<< HEAD
from kink import di, inject

=======
>>>>>>> a888b68e026857efbbacc1ef6a9a013ca4f55a22
from services.order_management.domain.entities.order import Order
from ..repository.order_repository import OrderRepository


@inject
class BaseOrderUsecase:
    def __init__(self,
                 repository: OrderRepository,
                 order: Order) -> None:
        self.repository = repository
        self.order = order
