import uvicorn
import os
from fastapi import FastAPI

from .di import init_di
from .presentation.apis.item import router

api_root_path = os.getenv('API_ROOT_PATH', '')
app = FastAPI(root_path=api_root_path)


@app.on_event("startup")
async def startup_event():
    await init_di()


app.include_router(router, prefix='')

uvicorn.run(app, host="0.0.0.0", port=6996)
