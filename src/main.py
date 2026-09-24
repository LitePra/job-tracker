from uuid import uuid4
from contextlib import asynccontextmanager

from sqlalchemy import create_engine, select, insert
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Mapped, mapped_column, Session
from fastapi import FastAPI, status, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s:     %(message)s")
DATABASE_URL = "postgresql+psycopg://postgres:admin@127.0.0.1:15432/postgres"
MAIN_TAG_GROUP = ["Job CRUD"]


engine = create_engine(DATABASE_URL)
Sessionlocal = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    id: Mapped[str] = mapped_column(primary_key=True, default= lambda: str(uuid4()))

class JobORM(Base):
    __tablename__ = "jobs"

    title: Mapped[str]
    stack: Mapped[str]
    experience: Mapped[int] = mapped_column(default=0)
    apply: Mapped[bool] = mapped_column(default=False)

@asynccontextmanager
async def lifespan(_: FastAPI):
    logging.info("Started")
    Base.metadata.create_all(bind=engine)
    yield
    logging.info("Finished")
app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000"],
    allow_methods=["*"]
)

class JobSchema(BaseModel):
    id: str
    title: str
    stack: str
    experience: int = 0
    apply: bool

class JobCreate(BaseModel):
    title: str
    stack: str
    experience: int = 0

class JobUpdate(BaseModel):
    title: str | None = None
    stack: str | None = None
    apply: bool | None = None

def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()

def job_to_model(job_orm: JobORM):
    return JobSchema(id=job_orm.id,title=job_orm.title,stack=job_orm.stack,experience=job_orm.experience,apply=job_orm.apply)

@app.get("/health",tags=["Health"])
def Health():
    """Checks server status"""
    return {"status": "active"}

@app.get("/jobs",tags=MAIN_TAG_GROUP)
def read_jobs(db: Session = Depends((get_db))) -> list[JobSchema]:
    jobs = db.scalars(select(JobORM)).all()
    return [job_to_model(job) for job in jobs]

@app.post("/jobs",status_code=status.HTTP_201_CREATED,tags=MAIN_TAG_GROUP)
def add_job(payload: JobCreate, db: Session = Depends((get_db))) -> JobSchema:
    new_job = JobORM(title=payload.title,stack=payload.stack,experience=payload.experience)
    db.add(new_job)
    db.commit()

    return job_to_model(new_job)

@app.patch("/jobs/{job_id}",tags=MAIN_TAG_GROUP)
def update_job(job_id: str, payload: JobUpdate, db: Session = Depends((get_db))) -> JobSchema:
    job_for_update = db.get(JobORM, job_id)
    if payload.title:
        job_for_update.title = payload.title
    if payload.stack:
        job_for_update.stack = payload.stack
    if payload.apply is not None:
        job_for_update.apply = payload.apply

    db.commit()

    return job_for_update
@app.delete("/jobs/{job_id}",status_code=status.HTTP_204_NO_CONTENT,tags=MAIN_TAG_GROUP)
def delete_job(job_id: str, db: Session = Depends((get_db))):
    job_for_delete = db.get(JobORM, job_id)
    db.delete(job_for_delete)

    db.commit()