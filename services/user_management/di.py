from .data.repository import UserRepositoryImpl
from .domain.repository import UserRepository
from .domain.usecases import *

from kink import di

async def init_di():
    repository = UserRepositoryImpl()
    await repository.init()

    di[UserRepository] = repository
