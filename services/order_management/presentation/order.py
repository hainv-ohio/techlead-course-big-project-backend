from fastapi import APIRouter, Depends

from ..domain.usecases.order_action import OrderAction

router = APIRouter()


@router.post('/{order_id}')
async def order(order_id: str,
<<<<<<< HEAD
                order_action: OrderAction = Depends(OrderAction)):
    
    return order_action.execute(order_id)
=======
                order_action: Depends(OrderAction)):
    return order_action.execute(order_id)
>>>>>>> a888b68e026857efbbacc1ef6a9a013ca4f55a22
