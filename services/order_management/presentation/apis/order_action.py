from urllib import response
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from ..schemas.base import BaseResponseSchema
from core.types import failure

from ...domain.usecases.get_order_usecase import GetOrderUsecase
from ...domain.usecases.update_time_pickup_usecase import UpdateTimePickupUsecase
from ..schemas.order_action import OrderPickupTimeRequest, OrderRespone

router = APIRouter()


@router.get('/{order_id}',
            name='Get order',
            description='Get order by ID',
            response_model=OrderRespone,
            responses={
                 400: {"model": BaseResponseSchema},
                 401: {"model": BaseResponseSchema}
            })
async def order_action(order_id: str,
                get_order_usecase: GetOrderUsecase = Depends(GetOrderUsecase)):
    order, failure = await get_order_usecase.execute(order_id)

    if failure is not None:
        return JSONResponse(
            status_code=failure.code,
            content={'status': 'not exist', 'message': "There is no Order"}
        )
    return {
        'status': 'success',
        'message': '',
        'data': {
            'id': order.id,
            'store_id': order.store_id,
            'customer_id': order.customer_id,
            'status': order.status,
            'created_at': order.created_at,
            'updated_at': order.updated_at,
            'take_time_from': order.take_time_from,
            'take_time_to': order.take_time_to
        }
    }

@router.post('/pickup-time',
            name='Pickup time',
            description='Add/Update pickup time for order',
            responses={
                 400: {"model": BaseResponseSchema},
                 401: {"model": BaseResponseSchema}
            })
async def pickup_time(data: OrderPickupTimeRequest,
                        update_time_pickup_usecase: UpdateTimePickupUsecase = Depends(lambda: UpdateTimePickupUsecase())):
    order, failure = await update_time_pickup_usecase.execute(order_id=data.order_id, take_time_from=data.take_time_from, take_time_to=data.take_time_to)
    if failure is not None:
        return JSONResponse(
            status_code=failure.code,
            content={'status': 'failure', 'message': "Can not choose take time!"}
        )
    return {
        'status': 'success',
        'message': '',
        'data': {
            'take_time_from': order.take_time_from,
            'take_time_to': order.take_time_to
        }
    }
