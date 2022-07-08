import json
from confluent_kafka import Consumer
from confluent_kafka import Producer
from uuid import uuid4


class Kafka:
    def __init__(self):
        pass

    async def send(self, topic, value):
        message = value.encode()
        print(message)
        producer = Producer({
            'bootstrap.servers': 'localhost:9092',
            'security.protocol': 'PLAINTEXT',
        })
        try:
            producer.produce(topic, str(uuid4()), message)
            producer.flush()
        except Exception as ex:
            print("Exception happened :", ex)
        # send message to kafka
        pass

    async def subscribe(self, topic):
        consumer = Consumer({
            'bootstrap.servers': 'localhost:9092',
            'auto.offset.reset': 'largest',
            'enable.auto.commit': 'false',
            'max.poll.interval.ms': '86400000'
        })
        consumer.subscribe(
            topic
        )
        return consumer.poll(0)
