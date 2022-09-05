from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from core.types import failure

from ...domain.usecases.get_order_usecase import GetOrderUsecase

router = APIRouter()


@router.get('/{order_id}')

async def get_order(order_id: str,
                get_order_usecase: GetOrderUsecase = Depends(GetOrderUsecase)):
    order, failure = await get_order_usecase.execute(order_id)

    print('api order', order)
    print('api failure', failure)

    if failure is not None:
        return JSONResponse(
            status_code=failure.code,
            content={'status': 'not exist', 'message': "There is no Order"}
        )
    return {
        'status': 'success',
        'message': '',
        'data': {
            'order_id': order.id,
            'store_id': order.store_id,
            'customer_id': order.customer_id,
            'status': order.status,
            'created_at': order.created_at,
            'updated_at': order.updated_at,
            'take_time_from': order.take_time_from,
            'take_time_to': order.take_time_to
        }
    }

async def pickupDate(order_id, date_time_pickup):
    
    pass 

