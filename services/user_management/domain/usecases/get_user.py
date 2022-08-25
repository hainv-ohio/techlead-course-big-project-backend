from .base import BaseUserUsecase


class GetUserUseCase(BaseUserUsecase):
    def __init__(self) -> None:
        super().__init__()

    async def execute(self, id):
        user = await self.repository.get_user_by_id(id)
        if user:
            self.repository.send_message_to_store(user)
        print(user)
        return user
