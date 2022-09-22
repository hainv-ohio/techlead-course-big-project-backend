from datetime import datetime
from fastapi import APIRouter, Depends

from ...domain.usecases.update_time_pickup_usecase import UpdateTimePickupUsecase

router = APIRouter()

@router.post('/add-to-cart/{data}')

async def pickupDate(data: str,
                    update_time_pickup_usecase: UpdateTimePickupUsecase = Depends(UpdateTimePickupUsecase)):    
    pass

    