from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models.base import Base
from db.session import engine
from api.routers.job import jobs_router
from api.routers.health import health_router


import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s:     %(message)s")

@asynccontextmanager
async def lifespan(_: FastAPI):
    logging.info("Started")
    Base.metadata.create_all(bind=engine)
    yield
    logging.info("Finished")
app = FastAPI(lifespan=lifespan)
app.include_router(router=jobs_router)
app.include_router(router=health_router)

app.add_middleware(
    CORSMiddleware,
    allow_methods=["*"]
)