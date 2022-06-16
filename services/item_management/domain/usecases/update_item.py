from kink import di, inject
from .base import BaseItemUsecase
from ..entities.item import Item

class UpdateItemUseCase(BaseItemUsecase):
    def __init__(self) -> None:
        super().__init__()

    async def execute(self, Item):
        pass