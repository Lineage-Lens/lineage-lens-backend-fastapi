from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from config import settings
from db import create_db_and_tables
from routers import person


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(person.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=settings.port)