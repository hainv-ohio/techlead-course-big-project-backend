from pydantic import BaseModel


class UserInfoResponse(BaseModel):
    name: str
    status: str
    phone: str

    class Config:
        schema_extra = {
            "example": {
                "name": "Haha",
                "status": "ACTIVE",
                "phone": "123455"
            }
        }
