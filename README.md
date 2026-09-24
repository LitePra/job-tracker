<<<<<<< HEAD
# job-tracker
=======
# Job Tracker API

A small REST API for managing job application records.

The project was developed with **FastAPI** and **PostgreSQL** and was also used as a practical **Manual QA training project**. The API was tested through Postman with additional database-level verification.

## Tech Stack

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- Postman
- Git / GitHub

## Project Structure

The project uses a layered structure to separate API, business logic, database access, and data models.

```
src/
├── api/
│   ├── dependencies.py
│   └── routers/
│       ├── health.py
│       └── job.py
├── core/
│   └── config.py
├── db/
│   └── session.py
├── models/
│   ├── base.py
│   └── job.py
├── repository/
│   └── job.py
├── schemas/
│   └── job.py
├── services/
│   └── job.py
└── main.py
```

## API Endpoints

| Method   | Endpoint         | Description      |
| -------- | ---------------- | ---------------- |
| `POST`   | `/jobs`          | Create a new job |
| `GET`    | `/jobs`          | Get all jobs     |
| `GET`    | `/jobs/{job_id}` | Get a job by ID  |
| `DELETE` | `/jobs/{job_id}` | Delete a job     |
| `GET`    | `/health`        | Check API health |

## QA Practice

The API was tested as a real QA practice project.

The testing process included:

- Requirements analysis
- Test planning
- Test design
- Positive and negative test scenarios
- Boundary value testing
- Input validation testing
- API testing with Postman
- Database-level verification
- Defect reporting
- Defect retesting
- Regression testing

### Test Execution

**16 test cases** were executed during the initial test execution.

The tests covered:

- Valid requests
- Missing required fields
- Empty values
- Whitespace-only values
- Invalid data types
- Unknown request fields
- Boundary values
- Existing and non-existing resources
- Invalid UUID formats
- Database state after API operations

The initial execution identified **10 defects**.

### Defects Found

The discovered defects included:

- Empty `title` and `stack` values were accepted.
- Whitespace-only `title` and `stack` values were accepted.
- Invalid `apply` values were accepted.
- Unknown request fields were accepted.
- Negative `experience` values were accepted.
- Invalid UUID formats returned `404` instead of `422`.

Seven defects were fixed and successfully verified during retesting.

### Retesting

After the fixes, the affected test cases were executed again.

**7 out of 7 retests passed.**

The retest confirmed that:

- Invalid empty values are rejected.
- Whitespace-only values are rejected.
- Invalid `apply` values are rejected.
- Unknown request fields are rejected.
- The database remains unchanged when invalid requests are rejected.

### Regression Testing

After the fixes, a regression test was performed on related functionality.

The regression suite covered:

- Valid job creation
- Existing input type validation
- Valid `experience` boundary values
- Retrieving all jobs
- Retrieving a job by ID
- Deleting a job

**5 out of 6 regression checks passed.**

The regression test revealed an additional defect:

> `GET /jobs` returns `500 Internal Server Error` when invalid existing records are present in the database.

The issue occurs because Pydantic response validation fails when these existing records are converted to the response schema.

This defect is documented as **BUG-011** and remains open.

## QA Documentation

The repository contains QA documentation covering the complete testing process:

```
qa/
├── requirements/
├── test-cases/
├── test-execution/
│   ├── execution.md
│   ├── retest.md
│   └── regression.md
└── bug-reports/
```

The documentation includes:

- Requirements
- Test Plan
- Test Cases
- Test Execution
- Bug Reports
- Retest Execution
- Regression Execution

## How to Run

### 1. Clone the repository

```
git clone <repository-url>
cd job-tracker
```

### 2. Create and activate a virtual environment

```
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Configure PostgreSQL

Create a PostgreSQL database and configure the required database connection settings.

### 5. Start the API

```
uvicorn src.main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

FastAPI documentation is available at:

```
http://127.0.0.1:8000/docs
```

## Project Status

The project is considered complete as a QA practice project.

The API was tested through the main CRUD operations, defects were documented and fixed, fixes were retested, and regression testing was performed.

One known defect remains open: **BUG-011**, related to invalid existing database records and response validation in `GET /jobs`.
>>>>>>> d5cfd74 (Add final QA documentation and testing)
