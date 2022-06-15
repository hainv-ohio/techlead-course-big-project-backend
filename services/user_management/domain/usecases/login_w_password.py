from typing import Tuple
from core.types import Failure
from services.user_management.domain import repository
from .base import BaseUserUsecase

from ..entities.user import User

class LoginWithPasswordUseCase(BaseUserUsecase):

    async def execute(self, email, password) -> Tuple[User, Failure]:
        user_credential, failure = await self.repository.login_with_password(email, password)
        self.repository.store_token(user_credential.token)
        return user_credential.user, failure

