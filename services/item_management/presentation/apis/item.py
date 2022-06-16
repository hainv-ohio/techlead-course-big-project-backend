

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from services.item_management.domain.usecases.get_by_id import GetItemUseCase

from ...domain.usecases import *

router = APIRouter()


@router.get('/{id}')
async def get_item_by_id(id: int,
                         get_item_by_id_usecase: GetItemUseCase = Depends(GetItemUseCase)):
    result = await get_item_by_id_usecase.execute(id)
    # return {'name': "Hello", 'phone': '123456'}
    return result
