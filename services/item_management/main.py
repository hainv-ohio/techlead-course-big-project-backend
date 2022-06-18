import uvicorn

from fastapi import FastAPI
from .presentation.apis.item import router

from .di import init_di

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    await init_di()

app.include_router(router, prefix='/item')

uvicorn.run(app, host="0.0.0.0", port=6996)