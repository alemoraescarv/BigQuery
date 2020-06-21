### UDF JavaScript

Subtract two arrays.

```sql
CREATE TEMP FUNCTION
  sub_arr (arr ARRAY<int64>)
  RETURNS int64
  LANGUAGE js AS '''
arr_sub=0
 for(var i = 0; i < arr.length; i++){
    arr_sub = parseInt(arr[i]) - arr_sub ;
  };
  return arr_sub;
''';

#Sample data
WITH
  data AS (
  SELECT [2, 7] AS some_array UNION ALL
  SELECT [10, 32] AS some_array UNION ALL
  SELECT [15,20] AS some_array )

#query using the UDF
SELECT sub_arr(some_array) AS result_diff
FROM data
```
