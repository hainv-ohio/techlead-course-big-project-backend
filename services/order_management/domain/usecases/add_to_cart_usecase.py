
from typing import Tuple

from core.types import Failure
from .base import BaseUsecase
from ..entities.order import Order



class AddToCartUsecase(BaseUsecase):
    def __init__(self) -> None:
        super().__init__()

    async def execute(self, data) -> Tuple[Order, Failure]:
        pass
        
        
        
