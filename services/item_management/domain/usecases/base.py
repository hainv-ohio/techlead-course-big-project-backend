from ..repository import ItemRepository
from kink import inject

@inject
class BaseItemUsecase:
    def __init__(self, repository: ItemRepository) -> None:
        self.repository = repository
