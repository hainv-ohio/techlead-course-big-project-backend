from locale import currency
from unicodedata import name
from urllib import response
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from core.types import failure
from services.order_management.domain.entities import cart_item
from ..schemas.base import BaseResponseSchema
from ...domain.usecases.get_order_usecase import GetOrderUsecase
from ...domain.usecases.update_time_pickup_usecase import UpdateTimePickupUsecase
from ...domain.usecases.add_item_to_cart_usecase import AddItemToCartUsecase
from ..schemas.order_action import OrderPickupTimeRequest, OrderRespone, OrderRequest, ItemRequest, CartItemRespone

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

@router.post('/add-to-cart',
            name='Add to cart',
            description='Add medicine to cart',
            # response_model=CartItemRespone,
            responses={
                 400: {"model": BaseResponseSchema},
                 401: {"model": BaseResponseSchema}
            })
async def add_item_to_cart(item_request: ItemRequest,
                            add_item_to_cart_usecase: AddItemToCartUsecase = Depends(lambda: AddItemToCartUsecase())):
    cart_item, failure = await add_item_to_cart_usecase.execute(item_id=item_request.item_id, customer_id=item_request.customer_id, qty=item_request.qty)
    if failure is not None:
        return JSONResponse(
            status_code=failure.code,
            content={'status': 'failure', 'message': "Can not add item to cart."}
        )
    return {
        'status': 'success',
        'message': '',
        'data': {
            "cart_id": cart_item.cart_id,
            "item_id": cart_item.item_id,
            "name": cart_item.name,
            "category_id": cart_item.category_id,
            "qty": cart_item.qty,
            "price": cart_item.price,
            "currency_code": cart_item.currency_code,
            "detail": cart_item.detail
        }
    }
