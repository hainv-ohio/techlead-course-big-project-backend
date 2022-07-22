
from .base import BaseUserUsecase
from core.utils import get_hashed_password

class UserResetPasswordUsecase(BaseUserUsecase):

    async def execute(self, user_id, old_password, new_password, cf_new_password):
        result, failure = self.repository.check_password(user_id=user_id, password=get_hashed_password(old_password))

        if failure is not None:
            return None, failure

        result, failure = self.repository.change_password(user_id=user_id, password=get_hashed_password(new_password))

        return result, failure

        