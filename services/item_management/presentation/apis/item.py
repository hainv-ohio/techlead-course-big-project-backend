from cmath import log
from fastapi import APIRouter, Depends

from ...domain.usecases.get_items_by_ids_usecase import GetItemsByIdsUsecase
from ...domain.usecases import *
from ..schema.base import *
from ..schema.item import *

getItemRouter = APIRouter()


@getItemRouter.get('/id/{id}')
async def get_item_by_id(id: str,
                         get_item_by_id_usecase: GetItemUseCase = Depends(GetItemUseCase)):
    result = await get_item_by_id_usecase.execute(id)
    if result is None:
        return {
            "status": "error",
            "message": "Product is not exist."
        }
    return {
        'status': 'success',
        'message': '',
        'data': {
            'id': result.id,
            'name': result.name,
            'sku': result.sku,
            'status': result.status,
            'category_id': result.category_id,
            'price': result.price,
            'currency_code': result.currency_code,
            'sort_description': result.sort_description,
            'long_description': result.long_description,
            'total_sale': result.total_sale,
            'brand_id': result.brand_id,
        }
    }


@getItemRouter.get('/get-items-by-ids/{ids}',
            responses={
                 400: {"model": BaseResponseSchema},
                 401: {"model": BaseResponseSchema}
            })
async def get_item_by_id(ids: str,
                        get_items_by_ids_usecase: GetItemsByIdsUsecase = Depends(lambda: GetItemsByIdsUsecase())):

    print('--- param ---')
    print(ids)

    items = await get_items_by_ids_usecase.execute(ids)
    if items is None:
        return {
            "status": "error",
            "code": 400,
            "message": "Can not get items"
        }
    data = []
    for item in items:
        data_item = {
            "id": str(item.id),
            "name": item.name,
            "sku": item.sku,
            "status": item.status,
            "category_id": item.category_id,
            "price": item.price,
            "currency_code": item.currency_code,
            "sort_description": item.sort_description,
            "long_description": item.long_description,
            "total_sale": item.total_sale,
            "brand_id": item.brand_id
        }
        data.append(data_item)
    
    return {
        "status": "success",
        "code": 200,
        "data": data
    }
