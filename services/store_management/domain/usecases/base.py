from kink import inject

from ..repository import StoreRepository
from ..repository import AddressRepository


@inject
class BaseStoreUsecase:
    def __init__(self, repository: StoreRepository, address_repository: AddressRepository) -> None:
        self.repository = repository
        self.address_repository = address_repository
