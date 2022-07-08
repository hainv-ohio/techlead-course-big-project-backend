from select import select
from fastapi import Depends
from .base import BaseUserUsecase
from ..repository.user_repository import UserRepository

class ReceiveMessageFromOrder(BaseUserUsecase):
    def __init__(self, 
                repository: UserRepository):
        super().__init__(repository)

    async def execute(self, order_id):
        self.repository.get_order_by_order_id(order_id=order_id)