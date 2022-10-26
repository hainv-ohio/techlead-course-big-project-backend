from dotenv import load_dotenv
load_dotenv('services/user_management/.env')
import uvicorn
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .config import cfg
from .di import init_di
from .presentation.apis.order_action import router as order_action

api_root_path = os.getenv('API_ROOT_PATH', '')
app = FastAPI(root_path=api_root_path)

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


app.include_router(order_router, prefix='')

uvicorn.run(app, host="0.0.0.0", port=6996)
