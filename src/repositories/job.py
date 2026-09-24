from sqlalchemy import select

from sqlalchemy.orm import Session

from models.job import JobORM


class JobRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> JobORM:
        return self.db.scalars(select(JobORM)).all()

    def get_by_id(self, job_id: str) -> JobORM:
        return self.db.get(JobORM, job_id)

    def create(self, title: str, stack: str, experience: int, apply: bool) -> JobORM:
        new_job = JobORM(title=title, stack=stack, experience=experience,apply=apply)
        self.db.add(new_job)
        return new_job

    def delete(self, JobORM) -> None:
        self.db.delete(JobORM)
