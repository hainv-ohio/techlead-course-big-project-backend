from kink import inject

from ..repository import ShopRepository


@inject
class BaseShopUsecase:
    def __init__(self, repository: ShopRepository) -> None:
        self.repository = repository
