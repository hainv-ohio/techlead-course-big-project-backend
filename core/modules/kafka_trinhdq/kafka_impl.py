from typing import Tuple

from core.types.failure import Failure
from .kafka import Kafka

class KafkaImpl(Kafka):
    def __init__(self) -> None:
        super().__init__()
    
    async def send(self, topic, value) -> Tuple[bool, Failure]:
        return self.producer_service.send(topic, value)

    async def subscribe(self, topic) -> Tuple[bool, Failure]:
        return self.consume_service.subscribe(topic)