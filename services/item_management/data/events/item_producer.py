import os
from .rabbitmq_module import RabbitMQ

class ItemProducer:
    def __init__(self, rabbitMQ: RabbitMQ):
        self.rabbitMQ = rabbitMQ
    
    async def send_item_message(self):
        self.rabbitMQ.connection
        self.rabbitMQ.publish('item', '', 'send item info')
        # self.rabbitMQ.close