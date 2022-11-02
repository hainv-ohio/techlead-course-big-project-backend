from typing import List
from pydantic import BaseModel
from datetime import datetime
from .base import BaseResponseSchema
from .order_info import OrderInfoResponse, OrderPickupTimeResponse



class OrderItemRequets(BaseModel):
    item_id: str
    qty: int
    price: float

    class Config:
        schema_extra = {
            "example": 
            {
                "item_id": "6fdc8d8b-4562-4d88-9347-be859e1f27b6",
                "qty": 1,
                "price": 299000
            }
        }



class OrderRequest(BaseModel):
    store_id: str
    customer_id: str
    status: int
    take_time_from: datetime
    take_time_to: datetime
    items: List[OrderItemRequets]
    class Config:
        schema_extra = {
            "example": 
            {
                'store_id': "914b1351-d474-4051-9e0a-4a67bdb56fe9",
                'customer_id': "3bb3c024-16f3-4077-b12b-f7ca4f0652cb",
                'status': 1,
                'take_time_from': '2022-09-22 16:41:48.890',
                'take_time_to': '2022-09-22 16:41:48.890',
                "items": 
                [
                    {
                        "item_id": "6fdc8d8b-4562-4d88-9347-be859e1f27b6",
                        "qty": 1,
                        "price": 299000
                    },
                    {
                        "item_id": "d3fb9c1a-740c-4404-9d6a-b642991a233a",
                        "qty": 1,
                        "price": 15000
                    },
                ]
            }
        }



class ItemRequest(BaseModel):
    item_id: str
    customer_id: str
    qty: int

    class Config:
        schema_extra = {
            "example": {
                "item_id": "ced5ff0f-88c8-4c98-9dab-11f91808f72b",
                "customer_id": "1h56gg7-f089-488b-a2c1-e5a9b1a59102",
                "qty": 1
            }
        }


class OrderPickupTimeRequest(BaseModel):
    id: str
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


#
# Respone Model
#
class OrderRespone(BaseResponseSchema):
    data: OrderInfoResponse
    class Config:
        schema_extra = {
            "example": {
                'id': 'ced5ff0f-88c8-4c98-9dab-11f91808f72b',
                'store_id': 1,
                'customer_id': 1,
                'status': 1,
                'created_at': '2022-09-22 16:41:48.890',
                'updated_at': '2022-09-22 16:41:48.890',
                'take_time_from': '2022-09-22 16:41:48.890',
                'take_time_to': '2022-09-22 16:41:48.890'
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


class CartItemRespone(BaseResponseSchema):
    cart_id: str
    name: str
    category_id: int
    price: float
    currency_code: str
    detail: str
    qty: int

    class Config:
        schema_extra = {
            "example": {
                "status": "success",
                "message": "Pick up time successfull",
                "data": {
                    "cart_id": "bb6c1814-3663-423e-9e12-5d7f5db29289",
                    "item_id": "ced5ff0f-88c8-4c98-9dab-11f91808f72b",
                    "name": "Test",
                    "category_id": 1,
                    "qty": 1,
                    "price": 10,
                    "currency_code": "dollar",
                    "detail": "Lorem"
                }
            }
        }
