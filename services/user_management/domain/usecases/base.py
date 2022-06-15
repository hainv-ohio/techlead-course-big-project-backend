from ..repository import UserRepository
from kink import inject

@inject
class BaseUserUsecase:
    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository
