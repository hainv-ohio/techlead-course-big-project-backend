import json
from confluent_kafka import Consumer
from confluent_kafka import Producer
from uuid import uuid4


class Kafka:
    def __init__(self):
        self.producer = self.init_producer()
        self.consumer = self.init_cusumer()
        pass

    async def send(self, topic, value):
        message = value.encode()
        print(message)
        try:
            self.producer.produce(topic, str(uuid4()), message)
            self.producer.flush()
        except Exception as ex:
            print("Producer Error :", ex)

    async def subscribe(self, topic):
        try:
            self.consumer.subscribe(
                topic
            )
            return self.consumer.poll(0)
        except Exception as ex:
            print("Producer Error :", ex)
        return None

    def init_producer(self):
        return Producer({
            'bootstrap.servers': 'localhost:9092',
            'security.protocol': 'PLAINTEXT',
        })

    def init_cusumer(self):
        return Consumer({
            'bootstrap.servers': 'localhost:9092',
            'auto.offset.reset': 'largest',
            'enable.auto.commit': 'false',
            'max.poll.interval.ms': '86400000'
        })
