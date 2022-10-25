from typing import Optional
from uuid import UUID
from pydantic import BaseModel
from datetime import datetime


class OrderInfoResponse(BaseModel):
    id: UUID
    status: int
    customer_id: str
    store_id: str
    take_time_from: Optional[datetime]
    take_time_to: Optional[datetime]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        schema_extra = {
            "example": {
                'id': '31c4c1c6-f089-488b-a2c1-e5a9b1a59102',
                'store_id': 1,
                'customer_id': 1,
                'status': 1,
                'created_at': '2022-09-22 16:41:48.890',
                'updated_at': '2022-09-22 16:41:48.890',
                'take_time_from': '2022-09-22 16:41:48.890',
                'take_time_to': '2022-09-22 16:41:48.890'
            }
        }


class OrderPickupTimeResponse(BaseModel):
    take_time_from: datetime
    take_time_to: datetime

    class Config:
        schema_extra = {
            "example": {
                'created_at': '2022-09-22 16:41:48.890',
                'updated_at': '2022-09-22 16:41:48.890'
            }
        }
