from typing import Tuple

from core.types.failure import Failure
from .base import BaseUserUsecase
from ..entities.user import User

class RegisterUserUsecase(BaseUserUsecase):

    async def execute(self, name, email, phone, password) -> Tuple[User, Failure]:
        if len(password) < 6:
            return None, Failure(400, "Weak password")
        user, failure = self.repository.register_user(
            full_name=name, 
            phone_number=phone, 
            email=email, 
            password=password
        )
        return user, failure