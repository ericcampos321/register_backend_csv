from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes import operator_routes
from src.config.env_config import env_config


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[env_config.FRONTEND_URL],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(operator_routes.router)