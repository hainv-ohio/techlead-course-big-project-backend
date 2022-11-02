from locale import currency
from multiprocessing.connection import wait
from unicodedata import name
from urllib import response
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from core.types import failure
from ...domain.entities import cart, cart_item
from ...domain.usecases import get_all_cart_items
from ..schemas.base import BaseResponseSchema
from ...domain.usecases.get_order_usecase import GetOrderUsecase
from ...domain.usecases.update_time_pickup_usecase import UpdateTimePickupUsecase
from ...domain.usecases.add_item_to_cart_usecase import AddItemToCartUsecase
from ...domain.usecases.get_all_cart_items import GetAllCartItems
from ...domain.usecases.place_order_usecase import PlaceOrderUsecase
from ...domain.usecases.get_cart_id_by_customer_id_usecase import GetCartIdByCustomerIdUsecase
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

@router.get('/get-all-cart-items/{cart_id}',
            name='Get cart items',
            description='Get all cart items',
            # response_model=CartItemRespone,
            responses={
                 400: {"model": BaseResponseSchema},
                 401: {"model": BaseResponseSchema}
            })
async def get_all_cart_items(cart_id: str,
                            get_all_cart_items: GetAllCartItems = Depends(lambda: GetAllCartItems())):
    cart_items = await get_all_cart_items.execute(cart_id=cart_id)
    result = []
    if cart_items is not None:
        for item in cart_items:
            print('-----Item-----')
            print(item)
            data = {
                "item_id": item.item_id,
                "name": item.name,
                "category_id": item.category_id,
                "qty": item.qty,
                "price": item.price,
                "currency_code": item.currency_code,
                "detail": item.detail
            }
            result.append(data)
    return result

@router.get('/get-cart-id-by-customer-id/{customer_id}',
            name='Get cart id by customer id',
            description='Get cart id by customer id',
            # response_model=CartItemRespone,
            responses={
                 400: {"model": BaseResponseSchema},
                 401: {"model": BaseResponseSchema}
            })
async def get_all_cart_items(customer_id: str,
                            get_cart_id_by_customer_id_usecase: GetCartIdByCustomerIdUsecase = Depends(lambda: GetCartIdByCustomerIdUsecase())):
    cart = await get_cart_id_by_customer_id_usecase.execute(customer_id=customer_id)
    if cart is None:
        return JSONResponse(
            status_code=401,
            content={'status': 'failure', 'message': "Customer does not have cart."}
        )
    return {
        'status': 'success',
        'message': '',
        'data': {
            "id": cart.id
        }
    }

@router.post('/place-order',
            name="Place Order",
            responses={
                 400: {"model": BaseResponseSchema},
                 401: {"model": BaseResponseSchema}
            })
async def place_order(data: OrderRequest,
                    place_order_usecase: PlaceOrderUsecase = Depends(lambda: PlaceOrderUsecase())):
    print('--- first order data ---')
    print(data)

    data = await place_order_usecase.execute(store_id=data.store_id, customer_id=data.customer_id, take_time_from=data.take_time_from, take_time_to=data.take_time_to, items=data.items)
    if data is not None:
        return {
            "code": 200,
            "status": "success",
            "message": "Order successful."
        }
