from kink import inject

from ..repository import StoreRepository


@inject
class BaseStoreUsecase:
    def __init__(self, repository: StoreRepository) -> None:
        self.repository = repository
