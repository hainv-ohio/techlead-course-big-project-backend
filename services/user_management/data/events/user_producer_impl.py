from core.types import Failure
from kafka import KafkaProducer
import json


class UserProducerImpl:

    async def get_user_success(self, user):
        producer = KafkaProducer(
            bootstrap_servers=['localhost:9092'],  # server name
            value_serializer=self.json_serializer  # function callable
        )
        producer.send(
            "get_user_success", user
        )

    async def json_serializer(self, user):
        json.dumps(user).encode('utf-8')
