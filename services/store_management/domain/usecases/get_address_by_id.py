from .base import BaseStoreUsecase


class GetAddressUseCase(BaseStoreUsecase):
    def __init__(self) -> None:
        super().__init__()

    async def execute(self, id):
        return await self.address_repository.get_address_by_id(id)
