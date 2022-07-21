from .base import BaseStoreUsecase


class MessageFromUser(BaseStoreUsecase):
    def __init__(self) -> None:
        super().__init__()

    async def execute(self, message):
        self.repository.receive_message_from_user(message)