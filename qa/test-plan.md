# TEST PLAN - Job Tracker

---
## Objective:
Verify that the Job Tracker API works according to requirements and that CRUD operations behave as expected.

## Scope:
- Job creation.
- Job retrieval.
- Job update.
- Job deletion.
- Input data validation.
- Data persistence in PostgreSQL 

## Test approach

**Testing types:** 
- Functional testing.
- Regression testing.
- Retesting.

**Testing levels:**
- Integration testing.

**Testing scope:**
- API testing.

**Tools:**
- Postman.
- PostgreSQL.

---
## Test environment
**Environment:**
- OS: Ubuntu 26.04.1 LTS.
- Backend: FastAPI.
- Database: PostgreSQL.
- Environment: Local development environment.

## Test data
**Valid data:**
- Java Developer / Java / 2.
- Front-end Developer / HTML, CSS, JavaScript / 1.
- Python Developer / Python, FastAPI / 0.

**Invalid data (according to requirements):**
- Experience < 0
- Missing required fields.
- Invalid field types.

> POST /jobs
```
{
    "title": "Java Backend Developer",
    "stack": "Java",
    "experience": 2
}
```
> GET /jobs/{job_id}
```
job_id: valid UUID
```
> PATCH /jobs/{job_id}
```
job_id: valid UUID
```
> DELETE /jobs/{job_id}
```
job_id: valid UUID
```

---
## Entry criteria
- API is available.
- Database is available.
- CRUD features are implemented.
- Requirements are approved.

## Exit criteria
- All planned test cases executed.
- No unresolved Critical/Blocker defects.
- All failed test cases investigated.
- Regression testing completed.
- Test results documented.

---
## Risks:
- Changing requirements.
