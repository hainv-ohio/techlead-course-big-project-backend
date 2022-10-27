from .base import BaseItemUsecase


class SendItemMessageUseCase(BaseItemUsecase):
    def __init__(self) -> None:
        super().__init__()

    async def execute(self, item):
        return await self.repository.send_item_message(item)
