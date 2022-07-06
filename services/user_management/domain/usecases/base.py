from kink import inject

from ..repository import UserRepository
from ..events.user_producer import UserProducer


@inject
class BaseUserUsecase:
    def __init__(self, repository: UserRepository, user_producer: UserProducer) -> None:
        self.repository = repository
        self.user_producer = user_producer
