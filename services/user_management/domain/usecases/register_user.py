from typing import Tuple

from core.types.failure import Failure
from .base import BaseUserUsecase
from ..entities.user import User

class RegisterUserUsecase(BaseUserUsecase):

    async def execute(self, first_name, last_name, email, phone_number, password) -> Tuple[User, Failure]:
        if len(password) < 6:
            return None, Failure(400, "Weak password")
        user, failure = await self.repository.register_user(
            User(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone_number=phone_number,
                is_created=True,
                is_verified=True
            ),
            password
        )
        return user, failure