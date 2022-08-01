

from kink import inject
from core.modules.messaging_module import MessagingModule

@inject
class UserProducer:
    def __init__(self, kafka: MessagingModule):
        self.kafka = kafka

    async def send_message_to_store(self, user):

        self.kafka.send("get_user_success", user)
