from .rabbitmq_module import RabbitMQ

class ItemProducer:
    def __init__(self, rabbitMQ: RabbitMQ):
        self.rabbitMQ = rabbitMQ
    
    async def send_item_message(rabbitMQ, item):
        rabbitMQ.connection
        rabbitMQ.publish(rabbitMQ, 'item', '', 'send item info')
        rabbitMQ.close