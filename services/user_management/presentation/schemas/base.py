from datetime import datetime

from pydantic import BaseModel

from core.utils.datetime_utils import format_utc_str


class BaseResponseSchema(BaseModel):
    status: str
    message: str
    data: dict

    class Config:
        json_encoders = {
            datetime: format_utc_str
        }
