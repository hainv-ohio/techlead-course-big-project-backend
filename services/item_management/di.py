from kink import di

from .data.repository import ItemRepositoryImpl
from .domain.repository import ItemRepository

from core.modules.messaging_module import MessagingModule, KafkaModule


async def init_di():
    # messaging_module = KafkaModule()
    # await messaging_module.init()

    # di[MessagingModule] = messaging_module

    repository = ItemRepositoryImpl()
    await repository.init()

    di[ItemRepository] = repository
