from .base import BaseItemUsecase


class GetItemsByIdsUsecase(BaseItemUsecase):
    def __init__(self) -> None:
        super().__init__()

    async def execute(self, ids):
        print('--- item usecase ---')
        print(ids)
        ids = ids.split("&")
        print(ids)
        return await self.repository.get_items_by_ids(ids=ids)
