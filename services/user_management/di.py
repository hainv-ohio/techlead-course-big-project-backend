from kink import di
from .data.repository import UserRepositoryImpl
from .domain.repository import UserRepository


async def init_di():
    repository = UserRepositoryImpl()

    await repository.init()

    di[UserRepository] = repository
