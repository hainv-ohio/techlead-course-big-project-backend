


"""
User Repository Interface
"""
from typing import List, Tuple
from ..entities.user import User
from core.types import Failure

class UserRepository:

    async def get_user_by_id(self, id) -> Tuple[User, Failure]:
        raise NotImplementedError()

    async def login_with_password(self, email: str, password: str) -> Tuple[User, Failure]:
        raise NotImplementedError()

    async def get_all_users(self) -> Tuple[List[User], Failure]:
        raise NotImplementedError()

    async def init(self):
        pass