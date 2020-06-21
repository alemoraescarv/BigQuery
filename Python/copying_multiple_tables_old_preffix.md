### Migrating multiple tables

In order to achieve what you aim, you wold have to use a DDL statement [CREATE TABLE][1] as follows: 

    CREATE TABLE 'project_id.dataset.table' AS SELECT * FROM `project_id.dataset.table_source`

However, it would not be possible to reference multiple destinations with wildcards. As stated in the documentation, [here][2], there are some limitations when using wildcards, among them:

> Queries that contain DML statements cannot use a wildcard table as the
> target of the query. For example, a wildcard table can be used in the
> FROM clause of an UPDATE query, but a wildcard table cannot be used as
> the target of the UPDATE operation.

Nonetheless, you can use the Python API to make a request to BigQuery. Then, save each view to a new table, each table's name with a new prefix and old suffix. You can do it as below: 

```python 
from google.cloud import bigquery

client = bigquery.Client()
dataset_id = 'your_dataset_id'

#list all the tables as objects , each obj has table.project,table.dataset_id,table.table_id
tables = client.list_tables(dataset_id) 

#initialising arrays (not necessary)
suffix=[]
table_reference=[]

#looping through all the tables in you dataset
for table in tables:
    
    #Filter if the table's name start with the prefix
    if "your_table_prefix" in table.table_id:
        
        #retrieves the suffix, which will be used in the new table's name
        #extracts the suffix of the table's name
        suffix=table.table_id.strip('your_table_prefix')
        
        #reference the source table
        table_reference=".".join([table.project,table.dataset_id,table.table_id])
        
        #table destination with new prefix and old suffix
        job_config = bigquery.QueryJobConfig()
        table_ref = client.dataset(dataset_id).table("_".join(['new_table_prefix',suffix]))
        job_config.destination = table_ref

        sql='''

            CREATE TEMP FUNCTION
              function_name ( <input> )
              RETURNS <type>
              LANGUAGE js AS """
                return <type>;
            """;

        SELECT function_name(<columns>) FROM `{0}`'''.format(table_reference)

        query_job = client.query(
            sql,
            # Location must match that of the dataset(s) referenced in the query
            # and of the destination table.
            location='US',
            job_config=job_config) 

        query_job.result()  # Waits for the query to finish
        print('Query results loaded to table {}'.format(table_ref.path))
```


Notice that in the `sql` query, first **'''** then **"""** were used in order to define the *query* and the *JS Temp Function*, respectively.

I would like to point that you have to make sure you environment has the appropriate packages to use the Python API for BigQuery, [here][3]. You can install the BigQuery package using: `pip install --upgrade google-cloud-bigquery`.
        


  [1]: https://cloud.google.com/bigquery/docs/tables#ddl
  [2]: https://cloud.google.com/bigquery/docs/reference/standard-sql/data-manipulation-language
  [3]: https://googleapis.dev/python/bigquery/latest/index.html



