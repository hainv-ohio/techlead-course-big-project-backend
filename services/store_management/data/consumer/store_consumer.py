from core.modules.kafka_module import Kafka
from ...domain.usecases.receive_message_from_user import MessageFromUser


class StoreConsumer:
    def __init__(self):
        self.kafka = Kafka()
        self.message = MessageFromUser()
        pass

    async def receive_message_from_user(self):
        result = self.kafka.subscribe('get_user_success')
        self.message.execute(result)
