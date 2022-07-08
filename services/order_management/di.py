from kink import di

from .data.repository.order_repository_impl import OrderRepositoryImpl
from .domain.repository.order_repository import OrderRepository
from core.modules.kafka_trinhdq.kafka_impl import KafkaImpl
from core.modules.kafka_trinhdq.kafka import Kafka

async def init_di():
    order_repository = OrderRepositoryImpl()
    kafka = KafkaImpl()
    await order_repository.init()
    await kafka.init()

    di[OrderRepository] = order_repository
    di[Kafka] = kafka
