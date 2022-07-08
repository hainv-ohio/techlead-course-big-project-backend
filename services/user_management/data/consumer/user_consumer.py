from fastapi import Depends
from core.modules.kafka_trinhdq.kafka import Kafka


class UserConsumer:
    def __init__(self,
                kafka: Kafka = Depends(Kafka)) -> None:
        self.kafka = kafka
    
    async def receive_message_from_user(self, topic):
        result = self.kafka.subscribe(topics=topic)
        return result