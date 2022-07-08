from confluent_kafka import Producer
import socket

from ...types.failure import Failure

class ProducerService:

    def __init__(self) -> None:
        pass

    def create_producer(self):
        conf = {'bootstrap.servers': '0.0.0.0:9092',
        'client.id': socket.gethostname()}

        return Producer(conf)

    def send(self, topic, key, value):
        producer = self.create_producer()
        producer.produce(topic, key=key, value=value)
        producer.flush()

    def acked(self, err, msg):
        if err is not None:
            return Failure(401, msg)
        else:
            return "Send message sucessfull."