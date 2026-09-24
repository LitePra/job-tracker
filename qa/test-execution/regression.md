# Regression Execution
## Regression Summary
|ID |Related Test Case | Status |Actual Result| Bug |
|---|------------------|--------|-------------|-----|
|REG-001|TC-001|**PASS**|201 returned; new job created in the database| -|
|REG-002|TC-006.1-006.3|**PASS**|422 returned; database unchanged| - |
|REG-003|TC-009.1-009.3|**PASS**|201 returned; new jobs created in the database| -|
|REG-004|TC-010|**FAIL**|500 returned|BUG-011|
|REG-005|TC-011|**PASS**|200 returned; job returned| -|
|REG-006|TC-014|**PASS**|204 returned; job deleted from the database| -|
# Details
## `REG-001`
**Related Test Case:** TC-001

**Regression Result:** PASS

### Actual Result:

- returned status code is 201 Created
- new job created in the database
---
## `REG-002`
**Related Test Case:** TC-006.1-006.3

**Regression Result:** PASS

### Actual Result:

- returned status code is 422 Unprocessable Entity
- database remains unchanged
---
## `REG-003`
**Related Test Case:** TC-009.1-009.3

**Regression Result:** PASS

### Actual Result:

- returned status code is 201 Created
- new jobs created in the database
---
## `REG-004`
**Related Test Case:** TC-010

**Regression Result:** FAIL

### Expected Result:

- returned list of all jobs
- returned status code is 200 OK

### Actual Result:
- no returned jobs
- returned status code is 500 Internal Server Error
---
## `REG-005`
**Related Test Case:** TC-011

**Regression Result:** PASS

### Actual Result:
- returned job
- returned status code is 200 OK
---
## `REG-006`
**Related Test Case:** TC-014

**Regression Result:** PASS

### Actual Result:
- job deleted from the database
- returned status code is 204 No Content
---