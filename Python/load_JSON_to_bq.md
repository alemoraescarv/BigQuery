### Loading JSON file to BigQuery

In order to load a JSON file to BigQuery, the JSON must be **New Line Delimited**. Below is an example in how to convert a JSON to New Line Delimited JSON.Then, upload it to BigQUery.

 1. Converting JSON to New Line Delimited JSON
```python 
import json
from google.cloud import bigquery

with open("json_data.json", "r") as read_file:
    data = json.load(read_file)
result = [json.dumps(record) for record in data]
with open('nd-proceesed.json', 'w') as obj:
    for i in result:
        obj.write(i+'\n')
```

 2. Continuing the above code, uploading it in BigQuery.
 
 ```python
 client = bigquery.Client()
filename = '/path/to/file.csv'
dataset_id = 'sample'
table_id = 'json_mytable'

dataset_ref = client.dataset(dataset_id)
table_ref = dataset_ref.table(table_id)
job_config = bigquery.LoadJobConfig()
job_config.source_format = bigquery.SourceFormat.NEWLINE_DELIMITED_JSON
job_config.autodetect = True

with open("nd-proceesed.json", "rb") as source_file:
    job = client.load_table_from_file(source_file, table_ref, job_config=job_config)

job.result()  # Waits for table load to complete.

print("Loaded {} rows into {}:{}.".format(job.output_rows, dataset_id, table_id))
 ```
 
 
