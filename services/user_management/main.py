from dotenv import load_dotenv
load_dotenv('services/user_management/.env')

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .config import cfg
import uvicorn

from .di import init_di
from .presentation.apis.user_auth import router as user_router

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


app.include_router(user_router, prefix='/user')

# uvicorn.run(app, host="0.0.0.0", port=6996)
