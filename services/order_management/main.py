from dotenv import load_dotenv
load_dotenv('services/user_management/.env')
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .config import cfg
from .di import init_di
from .presentation.apis.order_action import router as order_action

app = FastAPI()
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


app.include_router(order_action, prefix='/order')

uvicorn.run(app, host="0.0.0.0", port=6996)
