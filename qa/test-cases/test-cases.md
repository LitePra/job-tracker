# TC-001 - `POST /jobs` with valid data
## Preconditions
- API is running.
- Database is running.

## Test Data

```
{
    "title": "Java Backend Developer",
    "stack": "Java",
    "experience": 2
}
```

## Steps
1. Send a `POST` request to `/jobs` with the test data.
2. Verify response status-code.
3. Verify response body.
4. Query the database for the created job.
5. Verify that the created job exists in the database.

## Expected Result
1. Request is sent successfully.
2. Response status is `201 Created`
3. Response body contains:
```
{
    "id": valid UUID,
    "title": "Java Backend Developer",
    "stack": "Java",
    "experience": 2,
    "apply": false
}
```
4. The created job exists in the database with the same values.

---
# TC-002 - `POST /jobs` missing title
## Preconditions
- API is running.
- Database is running.

## Test Data

```
{
    "stack": "Java",
    "experience": 2
}
```

## Steps
1. Send a `POST` request to `/jobs` with the test data.
2. Verify response status-code
3. Verify that no new record was created in the database.

## Expected Result
1. Response status is `422 Unprocessable Entity`
2. The database state remains unchanged (no new record added).

---
# TC-003 - `POST /jobs` missing stack
## Preconditions
- API is running.
- Database is running.

## Test Data

```
{
    "title": "Java Backend Developer",
    "experience": 2
}
```

## Steps
1. Send a `POST` request to `/jobs` with the test data.
2. Verify response status-code
3. Verify that no new record was created in the database.

## Expected Result

1. Response status is `422 Unprocessable Entity`.
2. The database state remains unchanged (no new record added).

---
# TC-004 - `POST /jobs` empty data
## Preconditions
- API is running.
- Database is running.

## Test Data

|Case              |Payload                                                               |Expected Status|
|------------------|----------------------------------------------------------------------|---------------|
|Empty `title`     |{"title": "", "stack": "Java", "experience": 2}                       |422            |
|Empty `stack`     |{"title": "Java Backend Developer", "stack": "", "experience": 2}     |422            |
|Empty `experience`|{"title": "Java Backend Developer", "stack": "Java", "experience": ""}|422            |

## Steps
1. Send a `POST` request to `/jobs` for each test payload from the table.
2. Verify status code matches Expected Status.
3. Verify database remains unchanged.

---
# TC-005 - `POST /jobs` whitespace-only data
## Preconditions
- API is running.
- Database is running.

## Test Data

|Case                   |Payload                                                               |Expected Status|
|-----------------------|----------------------------------------------------------------------|---------------|
|Whitespace-only `title`|{"title": "      ", "stack": "Java", "experience": 2}                 |422            |
|Whitespace-only `stack`|{"title": "Java Backend Developer", "stack": "     ", "experience": 2}|422            |

## Steps
1. Send a `POST` request to `/jobs` for each test payload from the table.
2. Verify status code matches Expected Status.
3. Verify database remains unchanged.

---
# TC-006 - `POST /jobs` invalid types
## Preconditions
- API is running.
- Database is running.

## Test Data
|Case                     |Payload                                                                                |Expected Result|
|-------------------------|---------------------------------------------------------------------------------------|---------------|
|Invalid `title` type     |{"title": 54, "stack":"Java", "experience":2}                                          |422            | 
|Invalid `stack` type     |{"title": "Java Backend Developer", "stack": true, "experience":2}                     |422            |
|Invalid `experience` type|{"title": "Java Backend Developer", "stack": "Java", "experience": "five years"        |422            |
|Invalid `apply` type     |{"title": "Java Backend Developer", "stack": "Java", "experience": 2, "apply": "Soon"} |422            |

## Steps
1. Send a `POST` request to `/jobs` for each test payload from the table.
2. Verify status code matches Expected Status.
3. Verify database remains unchanged.

---
# TC-007 - `POST /jobs` unknown field
## Preconditions
- API is running.
- Database is running.

## Test Data

```
{
    "title": "Java Backend Developer",
    "stack": "Java",
    "experience": 2,
    "salary": 590
}
```
## Steps
1. Send a `POST` request to `/jobs` with the test data.
2. Verify response status-code.
3. Verify that no new record was created in the database.

## Expected Result

1. Response status is `422 Unprocessable Entity`.
2. The database state remains unchanged (no new record added).

---
# TC-008 - `POST /jobs` multiple unknown fields
## Preconditions
- API is running.
- Database is running.

## Test Data

```
{
    "title": "Java Backend Developer",
    "stack": "Java",
    "experience": 2,
    "salary": 590,
    "company": "Microsoft"
}
```
## Steps
1. Send a `POST` request to `/jobs` with the test data.
2. Verify response status-code.
3. Verify that no new record was created in the database.

## Expected Result

1. Response status is `422 Unprocessable Entity`.
2. The database state remains unchanged (no new record added).

---
# TC-009 - `POST /jobs` experience boundaries
## Preconditions
- API is running.
- Database is running.

## Test Data

|Case            |Payload                                              |Expected Status|
|----------------|-----------------------------------------------------|---------------|
|`experience` = 0|{"title": "Java", "stack": "Java", "experience": 0}  |201            |
|`experience` = 1|{"title": "Java", "stack": "Java", "experience": 1}  |201            |
|`experience` > 1|{"title": "Java", "stack": "Java", "experience": 5}  |201            |
|`experience` < 0|{"title": "Java", "stack": "Java", "experience": -5} |422            |


## Steps
1. Send a `POST` request to `/jobs` for each test payload from the table.
2. Verify status code matches Expected Status.

## Expected Result
1. `experience` = 0 - job is created.
2. `experience` = 1 - job is created.
3. `experience` > 1 - job is created.
4. `experience` < 0 - no job is created.

---