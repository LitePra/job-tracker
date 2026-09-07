from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel, field_validator


class Job(BaseModel):
    title: str
    company: str
    location: str
    salary: int
    @field_validator('salary')
    @classmethod
    def check_salary(cls, value: int) -> int:
        if value <= 0:
            raise ValueError("salary must be greater than 0")
        return value

app = FastAPI()
jobs_list = []
@app.post("/jobs")
def add_job(job: Job):
    jobs_list.append(job.model_dump())
    return jobs_list