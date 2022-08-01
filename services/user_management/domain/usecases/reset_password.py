
from .base import BaseUserUsecase
from core.utils import get_hashed_password

class UserResetPasswordUsecase(BaseUserUsecase):
    def __init__(self, salt) -> None:
        super().__init__()

        self.salt =salt

    async def execute(self, user_id, old_password, new_password, cf_new_password):
        result, failure = await self.repository.check_password(user_id=user_id, password=get_hashed_password(old_password, self.salt))

        if failure is not None:
            return None, failure

        result, failure = await self.repository.change_password(user_id=user_id, password=get_hashed_password(new_password, self.salt))

        return result, failure

        