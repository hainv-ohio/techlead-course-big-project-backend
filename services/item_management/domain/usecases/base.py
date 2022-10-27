from kink import inject

from ..repository import ItemRepository


@inject
class BaseItemUsecase:
    def __init__(self, repository: ItemRepository) -> None:
        self.repository = repository
