import uvicorn

from fastapi import FastAPI
from .presentation.order import router as order_router

from .di import init_di

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    await init_di()

app.include_router(order_router, prefix='/order')

uvicorn.run(app, host="0.0.0.0", port=6996)