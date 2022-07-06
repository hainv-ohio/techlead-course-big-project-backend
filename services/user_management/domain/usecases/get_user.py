from .base import BaseUserUsecase


class GetUserUseCase(BaseUserUsecase):
    def __init__(self) -> None:
        super().__init__()

    async def execute(self, id):
        user = await self.repository.get_user_by_id(id)
        if user is not None:
            get_user_success = await self.user_producer.get_user_success(user)
        else:
            pass
        return user
