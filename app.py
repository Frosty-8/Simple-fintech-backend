from fastapi import FastAPI
from database.db import initialize_database
from api.routes import router
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Initializing database.........")
    initialize_database()

    yield

    print("Application shutting down")


app = FastAPI(
    title="Fintech Wallet API",
    version="1.0.0",
    lifespan=lifespan
)


app.include_router(router)