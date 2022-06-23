from .base import BaseItemUsecase


class GetItemUseCase(BaseItemUsecase):
    def __init__(self) -> None:
        super().__init__()

    async def execute(self, id):
        return await self.repository.get_item_by_id(id)
