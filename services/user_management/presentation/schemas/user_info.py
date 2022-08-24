from pydantic import BaseModel


class UserInfoResponse(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone: str

    class Config:
        schema_extra = {
            "example": {
                "first_name": "Haha",
                "last_name": "Haha",
                "email": "ACTIVE",
                "phone": "123455"
            }
        }
