from core.types import Failure
from ..models import UserDAO
from ..consumer.user_consumer import UserConsumer
from ...domain.repository import UserRepository


class UserRepositoryImpl(UserRepository):
    def __init__(self) -> None:
        self.user_consumer = UserConsumer()
        super().__init__()

    async def get_user_by_id(self, id):
        # Access to db here
        return UserDAO.from_json({
            'name': "Haha",
            'phone': '123456'
        })

    async def login_with_password(self, email, password):
        if email == "abc@gmail.com" and password == "123":
            return UserDAO.from_json({
                'name': "Haha",
                'phone': '123456'
            }), None
        return None, Failure(401, "Incorrect username or password")
    
    async def get_order_by_order_id(self, order_id):
        result = self.user_consumer.receive_message_from_user(topic="get_order_by_id_action")

    
