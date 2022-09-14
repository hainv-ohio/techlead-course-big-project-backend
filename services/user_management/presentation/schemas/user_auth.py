from pydantic import BaseModel

from .base import BaseResponseSchema
from .user_info import UserInfoResponse


class UserPasswordLoginRequest(BaseModel):
    email: str
    password: str

    class Config:
        schema_extra = {
            "example": {
                "email": "abc@gmail.com",
                "password": "123",
            }
        }

class UserPasswordRegisterRequest(BaseModel):
    first_name: str
    last_name: str
    phone: str
    email: str
    password: str

    class Config:
        schema_extra = {
            "example": {
                "first_name": "Hana",
                "last_name": "Hana",
                "phone": "0123456789",
                "email": "abc@gmail.com",
                "password": "123",
            }
        }


class UserLoginResponse(BaseResponseSchema):
    data: UserInfoResponse

    class Config:
        schema_extra = {
            "example": {
                "status": "success",
                "message": "",
                "data": {
                    "name": "Haha",
                    "status": "ACTIVE",
                    "phone": "123455"
                }
            }
        }
