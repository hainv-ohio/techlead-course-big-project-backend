from typing import Tuple

from core.types import Failure
from .base import BaseUserUsecase
from ..entities.user import User


class LoginWithPasswordUseCase(BaseUserUsecase):

    async def execute(self, email, password) -> Tuple[User, str, Failure]:
        user_info, failure = await self.repository.login_with_password(email, password)
        token = 'Bearer abcxyz'
        return user_info, token, failure
