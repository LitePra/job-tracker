# TC-010 - `GET /jobs` with valid data
## Preconditions
- API is running.
- Database is running.

## Steps
1. Send a `GET` request to `/jobs`.
2. Verify response status-code.
3. Verify response body.
4. Compare returned jobs with records in the database.

## Expected Result
1. Request is sent successfully.
2. Response status is `200 OK`
3. Response body contains list of jobs.
4. Returned jobs and their fields match the corresponding records in the database.

---
# TC-011 - `GET /jobs/{job_id}` with valid data
## Preconditions
- API is running.
- Database is running.
- Job with `{job_id}` exists in the database.

## Test Data
`job_id = valid and existing in the database UUID`

## Steps
1. Send a `GET` request to `/jobs/{job_id}` with test data.
2. Verify response status-code.
3. Verify response body.
4. Compare returned job with record in the database.

## Expected Result
1. Request is sent successfully.
2. Response status is `200 OK`
3. Response body contains a job with requested `{job_id}`.
4. Returned job and its fields match the corresponding record in the database.

---
# TC-012 - `GET /jobs/{job_id}` with non-existing ID
## Preconditions
- API is running.
- Database is running.
- Job with `{job_id}` does not exist in the database.

## Test Data

`job_id = "66778a8a-99b1-1b2c-234c-45d66778d88e"`

## Steps
1. Send a `GET` request to `/jobs/{job_id}` with test data.
2. Verify response status-code.
3. Verify that the requested job does not persist in the database.

## Expected Result
1. Response status is `404 Not Found`
2. Requested job can not be found in the database.

---
# TC-013 - `GET /jobs/{job_id}` with invalid ID format
## Preconditions
- API is running.
- Database is running.

## Test Data

`job_id = "job_id_55"`

## Steps
1. Send a `GET` request to `/jobs/{job_id}` with test data.
2. Verify response status-code.
3. Verify the response body.

## Expected Result
1. Response status is `422 Unprocessable Entity`
2. Response body indicates that {job_id} has an invalid UUID format.

