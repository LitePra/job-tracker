# Retest Execution
## Retest Summary
|ID    |Test Case                                    |Bug    | Retest Result | Actual Result|
|------|---------------------------------------------|-------|---------------|--------------|
|RT-001|TC-004.1: `POST /jobs` empty `title`         |BUG-001|**PASS**       |422 returned  |
|RT-002|TC-004.2 `POST /jobs` empty `stack`          |BUG-002|**PASS**       |422 returned  |
|RT-003|TC-005.1 `POST /jobs` whitespace-only `title`|BUG-003|**PASS**       |422 returned  |
|RT-004|TC-005.2 `POST /jobs` whitespace-only `stack`|BUG-004|**PASS**       |422 returned  |
|RT-005|TC-006.4 `POST /jobs` invalid `apply` type   |BUG-005|**PASS**       |422 returned  |
|RT-006|TC-007 `POST /jobs` unknown field            |BUG-006|**PASS**       |422 returned  |
|RT-007|TC-008 `POST /jobs` multiple unknown fields  |BUG-007|**PASS**       |422 returned  |
# Details
## `RT-001` - `BUG-001`
**Related Test Case:** TC-004.1
**Retest Result:** PASS

### Actual Result:

- returned status code is 422 Unprocessable Entity
- database remains unchanged
---
## `RT-002` - `BUG-002`
**Related Test Case:** TC-004.2
**Retest Result:** PASS

### Actual Result:

- returned status code is 422 Unprocessable Entity
- database remains unchanged
---
## `RT-003` - `BUG-003`
**Related Test Case:** TC-005.1
**Retest Result:** PASS

### Actual Result:

- returned status code is 422 Unprocessable Entity
- database remains unchanged
---
## `RT-004` - `BUG-004`
**Related Test Case:** TC-005.2
**Retest Result:** PASS

### Actual Result:

- returned status code is 422 Unprocessable Entity
- database remains unchanged
---
## `RT-005` - `BUG-005`
**Related Test Case:** TC-006.4
**Retest Result:** PASS

### Actual Result:

- returned status code is 422 Unprocessable Entity
- database remains unchanged
---
## `RT-006` - `BUG-006`
**Related Test Case:** TC-007
**Retest Result:** PASS

### Actual Result:

- returned status code is 422 Unprocessable Entity
- database remains unchanged
---
## `RT-007` - `BUG-007`
**Related Test Case:** TC-008
**Retest Result:** PASS

### Actual Result:

- returned status code is 422 Unprocessable Entity
- database remains unchanged