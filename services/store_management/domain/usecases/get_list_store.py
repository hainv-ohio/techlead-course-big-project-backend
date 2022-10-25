from .base import BaseStoreUsecase


class GetListStoreUseCase(BaseStoreUsecase):
    def __init__(self) -> None:
        super().__init__()

    async def execute(self):
        return await self.repository.get_list_store()
