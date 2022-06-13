from ...domain.repository import UserRepository
from ...domain.entities.user import User
from ..models import DatabaseUser


class UserRepositoryImpl(UserRepository):
    def __init__(self) -> None:
        super().__init__()

    def get_user_by_id(self, id) -> User:
        # Access to db here
        return DatabaseUser({
          'name': "Haha",
          'phone': '123456'
        })