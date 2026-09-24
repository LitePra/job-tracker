from pydantic import BaseModel
from sqlalchemy.orm import Session

from repositories.job import JobRepository
from schemas.job import JobSchema, JobCreate, JobUpdate

class JobNotFound(Exception):
    """Job has not found in database"""
    pass

class JobService:
    def __init__(self, db: Session):
        self.db = db
        self.job_repository = JobRepository(db=db)

    def list_jobs(self) -> list[JobSchema]:
        jobs_orm = self.job_repository.get_all()
        return [JobSchema.model_validate(job) for job in jobs_orm]

    def job_by_id(self, job_id: str) -> JobSchema:
        jobs_orm = self.job_repository.get_by_id(job_id=job_id)
        if not jobs_orm:
            raise JobNotFound(f"Job with given id '{job_id}' has not found")
        return JobSchema.model_validate(jobs_orm)

    def create_job(self, job: JobCreate) -> JobSchema:
        job_orm = self.job_repository.create(job.title,job.stack,job.experience,job.apply)
        self.db.commit()
        return JobSchema.model_validate(job_orm)

    def update_job(self, job_id: str, job: JobUpdate) -> JobSchema:
        job_to_update = self.job_repository.get_by_id(job_id=job_id)
        if not job_to_update:
            raise JobNotFound(f"Job with given id '{job_id}' has not found")
        if job.title is not None:
            job_to_update.title = job.title
        if job.stack is not None:
            job_to_update.stack = job.stack
        if job.apply is not None:
            job_to_update.apply = job.apply
        self.db.commit()

        return JobSchema.model_validate(job_to_update)

    def delete_job(self, job_id: str) -> None:
        job_to_delete = self.job_repository.get_by_id(job_id=job_id)

        if not job_to_delete:
            raise JobNotFound(f"Job with given id '{job_id}' has not found")

        self.job_repository.delete(job_to_delete)
        self.db.commit()