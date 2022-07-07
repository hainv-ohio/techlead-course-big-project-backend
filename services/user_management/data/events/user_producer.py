from .....core.modules.kafka_module import Kafka


class UserProducer:
    def __init__(self, kafka: Kafka):
        self.kafka = kafka

    async def send_message_to_store(self, user):
        self.kafka.send("get_user_success", user)
