from .base import BaseItemUsecase


class GetItemsByCategory(BaseItemUsecase):
    def __init__(self) -> None:
        super().__init__()

    async def execute(self, id):
        return await self.repository.get_items_by_category_id(id=id)
