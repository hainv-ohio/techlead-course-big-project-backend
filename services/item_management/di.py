from kink import di

from .data.repository import ItemRepositoryImpl
from .domain.repository import ItemRepository

from core.modules.messaging_module import MessagingModule, KafkaModule


async def init_di():
    repository = ItemRepositoryImpl()
    await repository.init()

    messaging_module = KafkaModule()
    await messaging_module.init()

    di[MessagingModule] = messaging_module
    di[ItemRepository] = repository
