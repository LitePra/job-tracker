from fastapi import APIRouter, status, Depends, HTTPException

from api.dependencies import get_job_service
from services.job import JobService, JobNotFound
from core.config import get_settings
from schemas.job import JobSchema, JobUpdate, JobCreate


settings = get_settings()

jobs_router = APIRouter(prefix="/jobs")

@jobs_router.get("/",tags=settings.MAIN_TAG_GROUP)
def read_jobs(job_service: JobService = Depends(get_job_service)) -> list[JobSchema]:
    return job_service.list_jobs()

@jobs_router.get("/{job_id}",tags=settings.MAIN_TAG_GROUP)
def read_by_id(job_id: str, job_service: JobService = Depends(get_job_service)) -> JobSchema:
    try:
        return job_service.job_by_id(job_id=job_id)
    except JobNotFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

@jobs_router.post("/",status_code=status.HTTP_201_CREATED,tags=settings.MAIN_TAG_GROUP)
def add_job(payload: JobCreate, job_service: JobService = Depends(get_job_service)) -> JobSchema:
    return job_service.create_job(job=payload)

@jobs_router.patch("/{job_id}",tags=settings.MAIN_TAG_GROUP)
def update_job(job_id: str, payload: JobUpdate, job_service: JobService = Depends(get_job_service)) -> JobSchema:
    try:
        return job_service.update_job(job=payload,job_id=job_id)
    except JobNotFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

@jobs_router.delete("/{job_id}",status_code=status.HTTP_204_NO_CONTENT,tags=settings.MAIN_TAG_GROUP)
def delete_job(job_id: str, job_service: JobService = Depends(get_job_service)) -> None:
    try:
        return job_service.delete_job(job_id=job_id)
    except JobNotFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)