import json
from confluent_kafka import Producer
from uuid import uuid4
from typing import Any, Tuple
from core.types.failure import Failure

class ProducerService:
    ERR_CODE = 401
    ERR_CREATE_PRODUCER = "Can not create Producer"
    ERR_MESSAGE = "Can not send Message"

    def __init__(self) -> None:
        pass

    def create_producer(self) -> Tuple[Producer, Failure]:
        conf = {'bootstrap.servers': 'localhost:9092',
        'security.protocol': 'PLAINTEXT'}

        try:
            return Producer(conf)
        except Exception as ex:
            return Failure(self.ERR_CODE, self.ERR_CREATE_PRODUCER)

    def send(self, topic, key,value) -> Tuple[bool, Failure]:
        try:
            message = value.encode()
            producer = self.create_producer()
            producer.produce(topic, key=str(uuid4()), value=message)
            producer.flush()
            return True
        except Exception as ex:
            return Failure(self.ERR_CODE, self.ERR_MESSAGE)

    def acked(self, err, msg):
        if err is not None:
            return Failure(401, msg)
        else:
            return "Send message sucessfull."