import uvicorn
from fastapi import FastAPI

from .di import init_di
from .presentation.apis.get_order import router as get_order

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    await init_di()


app.include_router(get_order, prefix='/order')

# uvicorn.run(app, host="0.0.0.0", port=6996)
