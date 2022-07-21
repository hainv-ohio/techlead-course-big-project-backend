from fastapi import APIRouter, Depends

from ..domain.usecases.order_action import OrderAction

router = APIRouter()


@router.post('/{order_id}')
async def order(order_id: str,
                order_action: OrderAction = Depends(OrderAction)):
    
    return order_action.execute(order_id)
