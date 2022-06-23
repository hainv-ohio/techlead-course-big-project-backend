from fastapi import APIRouter, Depends

from ...domain.usecases import *

router = APIRouter()


@router.get('/{id}')
async def get_item_by_id(id: int,
                         get_item_by_id_usecase: GetItemUseCase = Depends(GetItemUseCase)):
    result = await get_item_by_id_usecase.execute(id)
    return result
