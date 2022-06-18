from fastapi import APIRouter,Depends
from ..domain.usecases.order_action import OrderAction
from ..domain.repository.order_repository import OrderRepository
from ..data.models.order_model import Order

router = APIRouter()

@router.post('/{order_id}')
async def order(order_id: str,
                order_action: Depends(OrderAction)):
    
    return order_action.execute(order_id)