from .base import BaseUserUsecase

class HandlerUserDeleteEvent(BaseUserUsecase):

    def __init__(self) -> None:
        super().__init__()

        self.repository.on_user_delete_event(self.on_user_delete)

    async def on_user_delete(self, data):
        pass
    
