from .data.repository import UserRepositoryImpl
from .domain.repository import UserRepository
from .domain.usecases import *
from core.modules.messaging_module import MessagingModule, KafkaModule

from kink import di

async def init_di():
    kafka_module = KafkaModule()
    di[MessagingModule] = kafka_module

    repository = UserRepositoryImpl()
    await repository.init()


    di[UserRepository] = repository
