### Merge

[Documentation:](https://cloud.google.com/bigquery/docs/reference/standard-sql/dml-syntax#merge_examples)
>If a row in the table to be updated joins with more than one row from the FROM clause, then the query generates the following runtime error: UPDATE/MERGE must match at most one source row for each target row.

 - * Attention: The above documentation states that you can have at most one match in the TARGET TABLE from each row in the SOURCE TABLE. In your case, you have actions which would have to occur in the same row. In other words, for the same pair of a and b in the TARGET TABLE , you have more than one match in the SOURCE TABLE. This can not happen when using MERGE.*
 
 ```sql
MERGE dataset.table_to_update T 
USING `project.dataset.source_table` S


WHEN MATCHED AND S.some_field = 'U' THEN
UPDATE SET 
T.a = S.a,
T.b = S.b,
T.n = S.n
WHEN MATCHED AND S.some_field = 'D' THEN
  DELETE
WHEN NOT MATCHED BY TARGET THEN
  INSERT 
  (a,b,n) 
VALUES
  (a,b,n)
 ```
