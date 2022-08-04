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
    @abstractmethod
    async def register_user(self, user: User, password: str) -> Tuple[User, Failure]:
        """
        Register a new User
        Return a new User (with ID)
        """
        raise NotImplementedError()
    @abstractmethod
    async def check_password(self, user_id, password) -> Tuple[User, Failure]:
        raise NotImplementedError()

    @abstractmethod
    async def change_password(self, user_id, password) -> Tuple[User, Failure]:
        raise NotImplementedError()
    @abstractmethod
    async def login_with_password(self, email: str, password: str) -> Tuple[User, Failure]:
        raise NotImplementedError()
    @abstractmethod
    async def get_all_users(self) -> Tuple[List[User], Failure]:
        raise NotImplementedError()
    @abstractmethod
    async def send_message_to_store(self, user: User) -> Tuple[List[User], Failure]:
        raise NotImplementedError()
