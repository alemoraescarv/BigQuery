### Parameterized query

As stated in the [documentation](https://cloud.google.com/bigquery/docs/parameterized-queries#using_timestamps_in_parameterized_queries), it is possible to use parameterized queries in BigQuery using the Command-Line interface (CLI). You need to use the flag --parameter within your bq query command in order to specify the varibles/parameters you will use.

This flag must be in the format name:type:value. Although, if type is omitted it will used as STRING. As an example:

```bash
timediff= $(bq query --use_legacy_sql=false 
--parameter='ts_value:TIMESTAMP:2016-12-07 08:00:00' 
--parameter='ts_value1:TIMESTAMP:2016-12-07 09:00:00' 
'SELECT
  TIMESTAMP_DIFF(@ts_value,@ts_value1, HOUR)')

echo $timediff
```

`--format=csv` can also be sued to change the output format.
