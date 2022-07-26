from datetime import datetime
from fastapi import APIRouter, Depends

from ...domain.usecases.update_time_pickup_usecase import UpdateTimePickupUsecase

router = APIRouter()

@router.post('/update-pickup-time/{order_id}/{pickup_datetime}')

async def pickupDate(order_id: str,
                    datetime_pickup: datetime,
                    update_time_pickup_usecase: UpdateTimePickupUsecase = Depends(UpdateTimePickupUsecase)):
    return await update_time_pickup_usecase.execute(order_id=order_id, datetime_pickup=datetime_pickup)

    