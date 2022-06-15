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