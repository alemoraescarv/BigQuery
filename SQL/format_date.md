###FORMAT_DATE()

This function receives a DATE and retrieves a DATE with another fomart according to a [formatting string](https://cloud.google.com/bigquery/docs/reference/standard-sql/date_functions#supported_format_elements_for_date).

[Documentation](https://cloud.google.com/bigquery/docs/reference/standard-sql/date_functions#format_date).

```sql
SELECT *
FROM `test-proj-261014.sample.test_*` 
where _TABLE_SUFFIX = FORMAT_DATE('%Y%m%d', CURRENT_DATE)
```
