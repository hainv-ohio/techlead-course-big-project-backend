from .base import BaseItemUsecase


class DeleteItemUseCase(BaseItemUsecase):
    def __init__(self) -> None:
        super().__init__()

    async def execute(self, id):
        pass
