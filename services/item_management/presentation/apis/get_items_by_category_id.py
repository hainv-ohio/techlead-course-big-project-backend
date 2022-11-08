from urllib import response
from fastapi import APIRouter, Depends
import json

from ...domain.usecases import *

getItemsByCategoryRouter = APIRouter()


@getItemsByCategoryRouter.get('/category/{id}')
async def get_items_by_category_id(id: str,
                         get_items_by_category_id: GetItemsByCategory = Depends(GetItemsByCategory)):
    result = await get_items_by_category_id.execute(id)
    data = []
    for item in result:
        item_data = {
            'id': item.id,
            'name': item.name,
            'sku': item.sku,
            'status': item.status,
            'category_id': item.category_id,
            'price': item.price,
            'currency_code': item.currency_code,
            'sort_description': item.sort_description,
            'long_description': item.long_description,
            'total_sale': item.total_sale,
            'brand_id': item.brand_id,
            'image': item.image
        }
        data.append(item_data)

    return {
        'status': 'success',
        'code': 200,
        'message': '',
        'data': data
    }
