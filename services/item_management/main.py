import uvicorn
import os
from fastapi import FastAPI

from .di import init_di
from .presentation.apis.item import getItemRouter
from .presentation.apis.send_message import sendMessageRouter

api_root_path = os.getenv('API_ROOT_PATH', '')
app = FastAPI(root_path=api_root_path)


@app.on_event("startup")
async def startup_event():
    await init_di()


app.include_router(getItemRouter, prefix='/item')
app.include_router(sendMessageRouter, prefix="/message")
# app.include_router(router, prefix='')

# uvicorn.run("services.item_management.main:app", host="0.0.0.0", port=6996, reload=True)
