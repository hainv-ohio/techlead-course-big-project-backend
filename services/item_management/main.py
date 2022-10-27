import os

from dotenv import load_dotenv

load_dotenv('services/item_management/.env')

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from .di import init_di
from .presentation.apis.item import getItemRouter as item_router

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


app.include_router(item_router, prefix='/item')

# uvicorn.run(app, host="0.0.0.0", port=6996)
