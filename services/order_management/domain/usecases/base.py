from kink import di, inject

from services.order_management.domain.entities.order import Order
from ..repository.order_repository import OrderRepository

@inject
class BaseOrderUsecase:
    def __init__(self, 
                 repository: OrderRepository,
                 order: Order) -> None:
        self.repository = repository
        self.order = order