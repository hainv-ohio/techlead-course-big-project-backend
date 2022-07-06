from kink import di
from .data.repository import UserRepositoryImpl
from .domain.repository import UserRepository
from .data.events import UserProducerImpl
from .domain.events import UserProducer
from .domain.usecases import *


async def init_di():
    repository = UserRepositoryImpl()
    await repository.init()

    di[UserRepository] = repository

    user_producer = UserProducerImpl()

    di[UserProducer] = user_producer
