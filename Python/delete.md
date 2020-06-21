### Copying multiple Partitioned tables

In order to copy mulitple partitioned tables within a time range using Shell, it is necessery to create a .csv file with the `bq commands` to copy each desired table. Then execute each command inside the file using bash.

The syntax is below, 

```shell
bq query --format=csv --nouse_legacy_sql '
SELECT
  CONCAT('bq cp -a `project_id:dataset.table', partition_name, 'project_id:dataset.partitioned_destination_table`)
FROM (
  SELECT
    DISTINCT FORMAT_DATETIME('%Y%m%d',
      CAST(_PARTITIONDATE AS datetime)) partition_name
  FROM
    `project_id.dataset.table'
  WHERE
    _PARTITIONTIME >= "start_date"
    AND _PARTITIONTIME < "end_date")' > output.csv
```

Then, to execute the commands inside the .csv, 

```bash
bash output.csv


SELECT
