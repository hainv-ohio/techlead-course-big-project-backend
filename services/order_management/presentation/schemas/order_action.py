from pydantic import BaseModel
from datetime import datetime
from .base import BaseResponseSchema
from .order_info import OrderInfoResponse, OrderPickupTimeResponse


class OrderPickupTimeRequest(BaseModel):
    order_id: str
    take_time_from: datetime
    take_time_to: datetime

    class Config:
        schema_extra = {
            "example": {
                "order_id": "ced5ff0f-88c8-4c98-9dab-11f91808f72b",
                "customer_id": "neo@gmail.com",
                "store_id": "1h56gg7-f089-488b-a2c1-e5a9b1a59102",
                "take_time_from": "2033-09-22 16:41:48.890",
                "take_time_to": "2033-09-22 16:41:48.890",
            }
        }


class OrderPickupTimeResponse(BaseResponseSchema):
    take_time_from: datetime
    take_time_to: datetime


    class Config:
        schema_extra = {
            "example": {
                "status": "success",
                "message": "Pick up time successfull",
                "data": {
                    "take_time_from": "132022-09-22 16:41:48.890",
                    "take_time_to": "132022-09-22 16:41:48.890"
                }
            }
        }
