import uvicorn 
from fastapi import FastAPI

from .di import init_di
from .presentation.apis.item import router

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    await init_di()


app.include_router(router, prefix='/item')

# uvicorn.run("services.item_management.main:app", host="0.0.0.0", port=6996, reload=True)
