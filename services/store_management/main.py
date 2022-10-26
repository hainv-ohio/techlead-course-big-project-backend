import os
from dotenv import load_dotenv

load_dotenv('services/store_management/.env')

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .di import init_di
from .presentation.apis.get_store import router as user_router
from .config import cfg

api_root_path = os.getenv('API_ROOT_PATH', '')
app = FastAPI(root_path=api_root_path)

origins = [
    '*'
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_event():
    await init_di()


app.include_router(user_router, prefix='')
