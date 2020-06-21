### Converting Python Dictionary to JSON

If you want to load a dictionary to BigQuery using Python, you have first to prepare your data. I chose to convert the Python Dictionary to a ***.json*** file and then load it to BigQuery using the Python API. However, according to the [documentation][1], BigQuery has some limitations regarding loading .json nested data, among them: 

 1. You .json must be new line delimited, that means that each object must be in a new line in the file
 2. BigQuery does not support maps or dictionaries in Json. Thus, in order to do so, you have to wrap your whole data in [], as you can see [here][1].

For this reason, some modifications should be done in the file, so you can load the created .json file to BiguQuery. I have created two scripts, in which: the first one converts the Pyhton dict to a JSON file and the second the JSON file is formatted as New Line delimited json and then loaded in BigQuery.

***Convert the python dict to a .json file. Notice that you have to wrap the whole data between []:***

```python
import json
from google.cloud import bigquery


py_dict =[{
'id': 123, 
'categories': [
    {'category': 'fruit', 'values': ['apple', 'banana']}, 
    {'category': 'animal', 'values': ['cat']},
    {'category': 'plant', 'values': []}
  ]
}]

json_data = json.dumps(py_dict, sort_keys=True)
out_file =  open('json_data.json','w+')
json.dump(py_dict,out_file)
```

***Second, convert json to new line delimited json and load to BigQuery:***

```python 
import json
from google.cloud import bigquery

with open("json_data.json", "r") as read_file:
    data = json.load(read_file)
result = [json.dumps(record) for record in data]
with open('nd-proceesed.json', 'w') as obj:
    for i in result:
        obj.write(i+'\n')
       

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

Then, in the BigQuery UI, you can query your table as follows:

    SELECT id, categories
    FROM `test-proj-261014.sample.json_mytable4` , unnest(categories) as categories

And the output:

[![enter image description here][2]][2]


  [1]: https://cloud.google.com/bigquery/docs/loading-data-cloud-storage-json#limitations
  [2]: https://i.stack.imgur.com/G2PsI.png
