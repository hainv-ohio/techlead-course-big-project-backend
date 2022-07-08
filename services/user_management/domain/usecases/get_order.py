from .base import BaseUserUsecase
from ..repository.user_repository import UserRepository

class GetOrder(BaseUserUsecase):
    def __init__(self, repository: UserRepository) -> None:
        super().__init__(repository)
    
    async def request_get_order_by_id(self, topic, order_id):
        pass
        
    
