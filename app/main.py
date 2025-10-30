import uvicorn
from fastapi import FastAPI

from config import settings


app = FastAPI()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=settings.port)