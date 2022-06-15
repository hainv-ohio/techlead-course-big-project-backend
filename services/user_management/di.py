
from kink import di
from .domain.repository import UserRepository
from .data.repository import UserRepositoryImpl

from .domain.usecases import *

async def init_di():
    repository =  UserRepositoryImpl()
    await repository.init()

    di[UserRepository] = repository