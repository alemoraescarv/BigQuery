### Creating Time inegstioned partitioned table.

In the below script, a time inegstion partitioned table is create using Shell. Also, it is valid to point that the data is being copied from the `bigquery-public-data.usa_names.usa_1910_current` public dataset. 

[Documentation.](https://cloud.google.com/bigquery/docs/creating-partitioned-tables#cli)

In terminal, 

```shell
bq query \
--destination_table your_project:your_dataset.partitioned_table \
--time_partitioning_type=DAY \
--use_legacy_sql=false \
'SELECT
   name,
   number
 FROM
   `bigquery-public-data`.usa_names.usa_1910_current
 WHERE
   gender = "M"
 ORDER BY
   number DESC'
```
