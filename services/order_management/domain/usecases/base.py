from kink import di, inject
from ..repository.order_repository import OrderRepository


@inject
class BaseUsecase:
    def __init__(self,
                 repository: OrderRepository) -> None:
        self.repository = repository
