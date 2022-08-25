from kink import inject
from core.modules.messaging_module import MessagingModule
from ...domain.usecases.receive_message_from_user import MessageFromUser

@inject
class StoreConsumer:
    def __init__(self, kafka: MessagingModule):
        self.kafka = kafka
        self.message = MessageFromUser()
        pass

    async def receive_message_from_user(self):
        result = self.kafka.subscribe('get_user_success')
        if result:
            self.message.execute(result)
