from .base import BaseStoreUsecase


class GetListStoreByAreaUsecase(BaseStoreUsecase):
    def __init__(self) -> None:
        super().__init__()

    async def execute(self, id):
        return await self.repository.get_list_store_by_area(id)