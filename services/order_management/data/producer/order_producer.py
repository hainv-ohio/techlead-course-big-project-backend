from fastapi import Depends
from core.modules.kafka_trinhdq.kafka import Kafka

class OrderProducer:
    def __init__(self,
                kafka: Kafka = Depends(Kafka)) -> None:
        self.kafka = kafka
    
    async def receive_message_from_user(self, topic):
        self.kafka.subscribe(topic=topic)
    
    async def send_message_to_user(self, topic, value):
        self.kafka.send(topic=topic, value=value)