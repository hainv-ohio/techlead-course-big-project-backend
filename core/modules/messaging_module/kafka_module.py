import asyncio
from uuid import uuid4

from confluent_kafka import Producer, Consumer
from confluent_kafka.admin import AdminClient, NewTopic

from .messaging_module import MessagingModule


class KafkaModule(MessagingModule):
    def __init__(self):
        pass

    async def init(self, *args, **kwargs):
        kafka_config = {
            'bootstrap.servers': 'localhost:9092',
            'security.protocol': 'PLAINTEXT',
        }
        admin_cfg = {}
        producer_cfg = {}
        consumer_cfg = {
            'auto.offset.reset': 'largest',
            'enable.auto.commit': 'false',
            'max.poll.interval.ms': '86400000'
        }
        admin_cfg.update(kafka_config)
        producer_cfg.update(kafka_config)
        consumer_cfg.update(kafka_config)

        self.admin = AdminClient(admin_cfg)
        self.producer = Producer(producer_cfg)
        self.consumer = Consumer(consumer_cfg)

        self.handlers = {} # Topic_key: {id: callback}

        asyncio.create_task(self._get_messages())

    async def _get_messages(self):

        while True:
            messages = self.consumer.consume(10, 0.1)

            if len(messages) == 0:
                continue

            for message in messages:
                topic = message.topic()
                key = message.key()
                value = message.value()

                handler_key = f'{topic}_{key}'
                if handler_key in self.handlers:
                    futures = []
                    for id, callback in self.handlers[handler_key].items():
                        futures.append(callback())
                    if len(futures) > 0:
                        await asyncio.gather(*futures)

    async def create_topics(self, topics, num_partition=5, replication_factor=1):
        self.admin.create_topics([NewTopic(topic, num_partition, replication_factor) for topic in topics])


    async def send(self, topic, data, key=None, *args, **kwargs):
        try:
            self.producer.produce(topic, key=key, value=data)
        except Exception as ex:
            print("Producer Error :", ex)

    async def subscribe(self, topic, id, callback, key=None, *args, **kwargs):
        try:
            handler_key = f'{topic}_{key}'
            if not handler_key in self.handlers:
                self.handlers[handler_key] = {}
            self.handlers[handler_key][id] = callback

            self.consumer.subscribe(topic)
        except Exception as ex:
            print("Producer Error :", ex)

    async def unsubscribe(self, topic, id, key=None, *args, **kwargs):
        handler_key = f'{topic}_{key}'
        if handler_key in self.handlers:
            if id in self.handlers[handler_key]:
                del self.handlers[handler_key][id]
            
        # TODO: If the topic have no key left, unsubscribe the topic
    
    async def flush(self, *args, **kwargs):
        self.producer.flush()
