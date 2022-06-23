from .base import BaseStoreUsecase


class GetBaseStoreUsecase(BaseStoreUsecase):
    def __init__(self) -> None:
        super().__init__()

    async def execute(self, id):
        return await self.repository.get_store_by_id(id)
