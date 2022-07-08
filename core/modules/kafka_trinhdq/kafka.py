from .consume_service import ConsumeService
from .producer_service import ProducerService
from typing import Tuple
from core.types.failure import Failure

class Kafka:
    def __init__(self, consume_service: ConsumeService(), producer_service: ProducerService()) -> None:
        self.consume_service = consume_service
        self.producer_service = producer_service

    async def send(self, topic, value) -> Tuple[bool, Failure]:
        raise NotImplementedError()

    async def subscribe(self, topics) -> Tuple[bool, Failure]:
        raise NotImplementedError()

    async def init(self):
        pass
    