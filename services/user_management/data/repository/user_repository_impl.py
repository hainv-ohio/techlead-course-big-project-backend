from typing import Tuple
from core.types import Failure
from ..dao import UserDAO
from ...domain.repository import UserRepository
from ...domain.entities.user import User
from ..orm import UserORM


class UserRepositoryImpl(UserRepository):
    def __init__(self) -> None:
        super().__init__()

        self.user_dao = UserDAO()

    async def init(self):
        from core.modules.sql_module import create_database_tables
        await create_database_tables()

    async def get_user_by_id(self, id):
        # Access to db here
        return self.user_dao.find_one(id=id)

    async def login_with_password(self, email, password) -> Tuple[User, Failure]:
        user = await self.user_dao.find_one(email=email, password=password)
        print('user', user)
        if user is not None:
            return user, None
        return None, Failure(401, "Incorrect username or password")

    async def register_user(self, user: User, password: str) -> Tuple[User, Failure]:
        user = UserORM(**{
            **user.to_json(keys=['first_name', 'last_name', 'phone_number', 'email', 'is_verified', 'profile_image_url', 'status']),
        })
        user.password = password
        await self.user_dao.save(user)
        return user, None
