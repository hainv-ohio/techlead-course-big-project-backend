import json

from kafka import KafkaProducer

from core.types import Failure
from ..models import UserDAO
from ...domain.repository import UserRepository


class UserRepositoryImpl(UserRepository):

    def __init__(self) -> None:
        super().__init__()

    async def get_user_by_id(self, id):
        # Access to db here
        return UserDAO.from_json({
            'name': "sdsdsdsd",
            'phone': '123456323232'
        })

    async def login_with_password(self, email, password):
        if email == "abc@gmail.com" and password == "123":
            return UserDAO.from_json({
                'name': "Haha",
                'phone': '123456'
            }), None
        return None, Failure(401, "Incorrect username or password")

    async def send_message_to_store(self, user):
        producer = KafkaProducer(
            bootstrap_servers=['localhost:9202'],
           api_version=(0, 10, 1))
        future = producer.send(
            "get_user_success", user
        )


