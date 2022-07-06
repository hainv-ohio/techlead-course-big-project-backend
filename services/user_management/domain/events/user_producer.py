from typing import List, Tuple

from core.types import Failure
from ..entities.user import User


class UserProducer:

    async def get_user_success(self, user) -> Tuple[bool, Failure]:
        raise NotImplementedError()
