### Family Clans in an Array

Getting family members and adding them to an unique array in one row. 

```sql
CREATE TEMP FUNCTION
  rel (relatives ARRAY<String>)
  RETURNS string
  LANGUAGE js AS '''
  return relatives;
''';

#provided data
WITH example_data AS(
  SELECT 'abc' AS relative_1, 'def' AS relative_2
  UNION ALL
  SELECT 'abc' AS relative_1, '123' AS relative_2
  UNION ALL
  SELECT 'def' AS relative_1, '334' AS relative_2
  UNION ALL
  SELECT 'fdc' AS relative_1, '123' AS relative_2
  UNION ALL
  SELECT 'fgl' AS relative_1, '342' AS relative_2
),

#Manipulating the data
data AS 
(
  SELECT
    t2.key,
    ARRAY_AGG(CAST(relative_2 AS string) ) AS relatives 
  FROM example_data t1
  LEFT JOIN ( SELECT DISTINCT relative_1 AS key FROM example_data
    GROUP BY relative_1) t2
  ON key=relative_1
  GROUP BY 1
  ORDER BY key 
)

#selecting the desired fields and using the UDF
SELECT key, rel(relatives) AS list_of_relatives FROM data
ORDER BY key
```

As you can see, the first step was to create a [UDF][1], which receives the nested field of Strings and simply return them in a list of strings for each "**Key**". After declaring the ***example_data***, in *step 2*, some data manipulation had to be performed. In order to achieve a table as following: 

[![enter image description here][2]][2]

As you can see, the table has the *relative_1* (***named as key***) and the relatives in a nested column. 

After that, the desired fields are selected. That means, **key** and the *UDF* as ***list_of_relatives***, which was written in the first step and the output is as below: 

[![enter image description here][3]][3]


Finally, notice that the ***list_of_relatives*** is not a nested field anymore. Instead,it is a *String* with each value separated by comma. As shown below:

[![enter image description here][4]][4]




  [1]: https://cloud.google.com/bigquery/docs/reference/standard-sql/user-defined-functions
  [2]: https://i.stack.imgur.com/T6vX9.png
  [3]: https://i.stack.imgur.com/U8AOA.png
  [4]: https://i.stack.imgur.com/LINlh.png
