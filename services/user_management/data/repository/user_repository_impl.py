from typing import Tuple
from core.types import Failure
from ..producer.user_producer import UserProducer
from ..dao import UserDAO
from ...domain.repository import UserRepository
from ...domain.entities.user import User



class UserRepositoryImpl(UserRepository):
    def __init__(self) -> None:
        self.user_producer = UserProducer()
        super().__init__()
        self.user_dao = UserDAO()

    async def get_user_by_id(self, id):
        # Access to db here
        return self.user_dao.find_one(id=id)

    async def login_with_password(self, email, password) -> Tuple(User, Failure):
        return None, Failure(401, "Incorrect username or password")

    async def send_message_to_store(self, user):
        self.user_producer.send_message_to_store(user)
