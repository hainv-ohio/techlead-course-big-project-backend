import uvicorn
from fastapi import FastAPI

from .di import init_di
from .presentation.apis.user_auth import router as user_router

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    await init_di()


app.include_router(user_router, prefix='/user')

# uvicorn.run(app, host="0.0.0.0", port=6996)
