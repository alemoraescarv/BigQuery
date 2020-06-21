### Update

Simple use case with [UPDATE](https://cloud.google.com/bigquery/docs/reference/standard-sql/dml-syntax#update_statement) and [REGEX_REPLACE()](https://cloud.google.com/bigquery/docs/reference/standard-sql/functions-and-operators#regexp_replace). It updates the specified field witht the value retrieved from the REGEX_REPLACE() function.

Syntax is below, 

```sql
UPDATE dataset.table
SET field_to_be_updated = REGEXP_REPLACE(field_to_be_updated, r"(\.[0-9]+)$", ".0")
#it is required to have an logical evaluation when using update
#in this case always perform the update.
WHERE TRUE
```
