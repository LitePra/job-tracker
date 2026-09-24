# Test Execution

## Execution Summary

|ID      |Test Case                             |Status  | Actual Result                |Bug    |
|--------|--------------------------------------|------- |------------------------------|-------|
|TC-001  |`POST /jobs` with valid data          |**PASS**|201 returned; job created     |-      |
|TC-002  |`POST /jobs` missing title            |**PASS**|422 returned; DB unchanged    |-      |
|TC-003  |`POST /jobs` missing stack            |**PASS**|422 returned; DB unchanged    |-      |
|TC-004.1|`POST /jobs` empty `title`            |**FAIL**|201 returned; job created     |BUG-001|
|TC-004.2|`POST /jobs` empty `stack`            |**FAIL**|201 returned; job created     |BUG-002|
|TC-004.3|`POST /jobs` empty `experience`       |**PASS**|422 returned; DB unchanged    |-      |
|TC-005.1|`POST /jobs` whitespace-only `title`  |**FAIL**|201 returned; job created     |BUG-003|
|TC-005.2|`POST /jobs` whitespace-only `stack`  |**FAIL**|201 returned; job created     |BUG-004|
|TC-006.1|`POST /jobs` invalid `title` type     |**PASS**|422 returned; DB unchanged    |-      |
|TC-006.2|`POST /jobs` invalid `stack` type     |**PASS**|422 returned; DB unchanged    |-      |
|TC-006.3|`POST /jobs` invalid `experience` type|**PASS**|422 returned; DB unchanged    |-      |
|TC-006.4|`POST /jobs` invalid `apply` type     |**FAIL**|201 returned; job created     |BUG-005|
|TC-007  |`POST /jobs` unknown field            |**FAIL**|201 returned; job created     |BUG-006|
|TC-008  |`POST /jobs` multiple unknown fields  |**FAIL**|201 returned; job created     |BUG-007|
|TC-009.1|`POST /jobs` `experience` = 0         |**PASS**|201 returned; job created     |-      |
|TC-009.2|`POST /jobs` `experience` = 1         |**PASS**|201 returned; job created     |-      |
|TC-009.3|`POST /jobs` `experience` > 1         |**PASS**|201 returned; job created     |-      |
|TC-009.4|`POST /jobs` `experience` < 0         |**FAIL**|201 returned; job created     |BUG-008|
|TC-010  |`GET /jobs`                           |**PASS**|200 returned; jobs exist in DB|-      |
|TC-011  |`GET /jobs/{job_id}` with valid data   |**PASS**|200 returned; job exists in DB|-      |
|TC-012  |`GET /jobs/{job_id}` with non-existing ID|**PASS**|404 returned; job does not exist in DB|-|
|TC-013  |`GET /jobs/{job_id}` with invalid ID format|**FAIL**|404 returned; job does not exist in DB|BUG-009|
|TC-014  |`DELETE /jobs/{job_id}` with valid data   |**PASS**|204 returned; job deleted from DB|-|
|TC-015  |`DELETE /jobs/{job_id}` with non-existing ID|**PASS**|404 returned; job does not exist in DB|-|
|TC-016  |`DELETE /jobs/{job_id}` with invalid ID format|**FAIL**|404 returned; job does not exist in DB|BUG-010|

