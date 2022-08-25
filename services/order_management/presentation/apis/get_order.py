from fastapi import APIRouter, Depends

from ...domain.usecases.get_order_usecase import GetOrderUsecase

router = APIRouter()


@router.get('/{order_id}')

async def get_order(order_id: str,
                get_order_usecase: GetOrderUsecase = Depends(GetOrderUsecase)):
    result = await get_order_usecase.execute(order_id)
    return result

async def pickupDate(order_id, date_time_pickup):
    
    pass

