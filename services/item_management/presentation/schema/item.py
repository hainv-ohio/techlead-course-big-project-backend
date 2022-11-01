from pydantic import BaseModel
from datetime import datetime
from .base import BaseResponseSchema

class GetItemsRequest(BaseModel):
    ids: dict

    class Config:
        schema_extra = {
            "example": {
                "ids": {0: '91ef56c2-0e98-419c-aba5-8b1da70b02c1', 1: 'e2b40be1-a7af-42b9-a625-024bce0208e7'}
            }
        }
