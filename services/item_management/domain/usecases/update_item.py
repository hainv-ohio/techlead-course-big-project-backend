from .base import BaseItemUsecase


class UpdateItemUseCase(BaseItemUsecase):
    def __init__(self) -> None:
        super().__init__()

    async def execute(self, Item):
        pass
