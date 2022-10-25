from abc import abstractmethod
from typing import Tuple

from core.types import Failure
from ..entities.address import Address


class AddressRepository:
    async def init(self):
        pass

    @abstractmethod
    async def get_address_by_id(self, id) -> Tuple[Address, Failure]:
        raise NotImplementedError()
