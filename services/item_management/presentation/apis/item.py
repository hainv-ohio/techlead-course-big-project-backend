from fastapi import APIRouter, Depends

from ...domain.usecases import *

getItemRouter = APIRouter()


@getItemRouter.get('/id/{id}')
async def get_item_by_id(id: str,
                         get_item_by_id_usecase: GetItemUseCase = Depends(GetItemUseCase)):
    result = await get_item_by_id_usecase.execute(id)
    return result
