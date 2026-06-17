from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware

from database.db import initialize_database
from api.routes import router


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

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

from fastapi.routing import APIRoute

print("\nALL ROUTES")
for route in app.routes:
    print(type(route), getattr(route, "path", None))