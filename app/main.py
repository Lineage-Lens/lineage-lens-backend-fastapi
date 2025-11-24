from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config import settings
from db import create_db_and_tables
from middleware.auth import AuthMiddleware
from routers import person, relationship


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
app.add_middleware(
    AuthMiddleware,
    client_id=settings.google_oauth2_client_id
)

app.include_router(person.router)
app.include_router(relationship.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=settings.port)