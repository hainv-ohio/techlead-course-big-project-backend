from .base import BaseUserUsecase


class GetUserUseCase(BaseUserUsecase):
    def __init__(self) -> None:
        super().__init__()

    async def execute(self, id):
        user = await self.repository.get_user_by_id(id)
        if user is not None:
            is_send_message_to_store = await self.repository.send_message_to_store(user)
        else:
            pass
        return user
