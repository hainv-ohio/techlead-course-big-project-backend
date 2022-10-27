from fastapi import APIRouter, Depends

from ...domain.usecases import *

sendMessageRouter = APIRouter()


@sendMessageRouter.get('/{id}')
async def send_message(id: int,
                         send_item_message: SendItemMessageUseCase = Depends(SendItemMessageUseCase)):
    result = await send_item_message.execute(id)
    return "Done"
