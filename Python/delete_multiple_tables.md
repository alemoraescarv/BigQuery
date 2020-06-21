### Deleting multiple tables

While in the [documentation](https://cloud.google.com/bigquery/docs/managing-tables#deleting_tables) it is stated that you can delete only one table at a time, it is possible to make an API request with a Python script in order to delete all the tables inside a dataset.

```python
from google.cloud import bigquery

#construct BigQuery client object
client = bigquery.Client()

#select your dataset and list the tables within it 
dataset_id='project_id.dataset'
tables = client.list_tables(dataset_id)  

#inititalizing the list of tables
list_tables=[]
    
for table in tables:
    #Create a list with the able reference for deletion 'project.dataset_id.table_id'
    id =".".join([table.project,table.dataset_id,table.table_id])
    list_tables.append(id)
    
    #List of tables
    print(list_tables)

#Delete all the tables inside the list of tables     
for table in list_tables:
    #print(table)
    client.delete_table(table)
    
print("{} {}".format("Number of deleted tables in the dataset:", len(list_tables)))
```
