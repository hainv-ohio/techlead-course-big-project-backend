

from core.modules.messaging_module import Kafka


class UserProducer:

    def __init__(self):
        self.kafka = Kafka()
        pass

    async def send_message_to_store(self, user):

        self.kafka.send("get_user_success", user)
