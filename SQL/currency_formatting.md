### How to format currency

The below SQL query shows one method on formatting a decimal number as currency. 

```sql
WITH
  data AS (
  SELECT
    20.21 AS num
  UNION ALL
  SELECT
    99999999.12 AS num
  UNION ALL
  SELECT
    12345 AS num )
  SELECT
  CONCAT('$ ',FORMAT("%'.2f", num)) AS new_num
  FROM
  data
```
