# Testing checklist

---
## CL-001 - `POST /jobs`

## Happy path
- Valid request 
- Correct response body
- 201 Created
- Job exists in DB
- Missing experience

## Negative
(expected: 422 Unprocessable Entity)
### Required fields
- Missing title 
- Missing stack

### Empty values
- Empty title
- Empty stack
- Empty experience
- Whitespace-only title
- Whitespace-only stack

### Types
- Invalid title type
- Invalid stack type
- Invalid experience type
- Invalid apply type

### Additional fields
- Unknown field
- Multiple unknown fields

## Experience boundaries
- experience = 0 (expected: 201 Created)
- experience = 1 (expected: 201 Created)
- experience > 1 (expected: 201 Created)
- experience < 0 (expected: 422 Unprocessable Entity)

---
## CL-002 - `GET /jobs`

## Positive
- Correct response body
- 200 OK
- Returned jobs matches DB records
---
## CL-003 - `GET /jobs/{job_id}`

## Positive
- Valid request
- Correct response body
- 200 OK
- Returned job matches DB record

# Negative
- Non-existing ID (expected: 404 Not Found)
- Invalid ID format (expected: 422 Unprocessable Entity)

---
## CL-004 - `DELETE /jobs/{job_id}`

## Positive
- Valid request
- 204 No Content
- Job no longer exists in DB

## Negative
- Non-existing ID (expected: 404 Not Found)
- Invalid ID format (expected: 422 Unprocessable Entity)
