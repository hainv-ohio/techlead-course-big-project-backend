from fastapi import APIRouter, Depends

from ...domain.usecases import *

getItemRouter = APIRouter()


@getItemRouter.get('/id/{id}')
async def get_item_by_id(id: str,
                         get_item_by_id_usecase: GetItemUseCase = Depends(GetItemUseCase)):
    result = await get_item_by_id_usecase.execute(id)

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
