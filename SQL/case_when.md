###Case When Statement

It evaulates if a logical expression is true and it `do something`, creating a new column. 

[Documentation.](https://cloud.google.com/bigquery/docs/reference/standard-sql/conditional_expressions)

In the example below, the Firebase public Dataset is being used. In addition, [UNNEST](https://cloud.google.com/bigquery/docs/reference/standard-sql/arrays#flattening_arrays) is used so it is possible to evaulate the nested fields within the param column.

```sql
WITH
  temporary_table AS(
  SELECT
    *,
    param
  FROM
    `firebase-public-project.analytics_153293282.events_20181003`,
    UNNEST(event_params) AS param )
SELECT
  *,
  CASE
    WHEN (param.key IN ('value', 'board')) THEN TRUE
END
  AS check
FROM
  temporary_table
LIMIT
  100;
```
