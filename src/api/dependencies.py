from fastapi import Depends
from sqlalchemy.orm import Session

from db.session import get_db
from services.job import JobService


def get_job_service(db: Session = Depends(get_db)):
    return JobService(db)
