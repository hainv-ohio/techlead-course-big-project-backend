from fastapi import APIRouter, Depends

from ...domain.usecases import *

getItemsByCategoryRouter = APIRouter()


@getItemsByCategoryRouter.get('/category/{id}')
async def get_items_by_category_id(id: int,
                         get_items_by_category_id: GetItemsByCategory = Depends(GetItemsByCategory)):
    result = await get_items_by_category_id.execute(id)
    return result
