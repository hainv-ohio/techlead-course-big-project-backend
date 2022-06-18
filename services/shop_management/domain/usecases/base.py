from ..repository import ShopRepository
from kink import inject

@inject
class BaseShopUsecase:
    def __init__(self, repository: ShopRepository) -> None:
        self.repository = repository
