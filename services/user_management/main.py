import uvicorn

from fastapi import FastAPI
from .presentation.user_auth import router as user_router

app = FastAPI()

app.include_router(user_router, prefix='/user')

uvicorn.run(app, host="0.0.0.0", port=6996)