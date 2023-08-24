"""
User Repository Interface
"""
from abc import abstractmethod
from typing import List, Tuple

from core.types import Failure
from ..entities.user import User



class UserRepository:
    
    async def init(self):
        pass
    
    @abstractmethod
    async def get_user_by_id(self, id) -> Tuple[User, Failure]: raise NotImplementedError()
    
    