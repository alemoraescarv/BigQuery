You can get convert your table schema to json simply using the [schema_to_json()][1] method. It needs two attributes, *schema_list* and *destination*, respectively. 

I exemplified your case using a public dataset with nested data and used [StringIO()][2] just to show how the schema will be.

```python
from google.cloud import bigquery
import io

client = bigquery.Client()

project = 'bigquery-public-data'
dataset_id = 'samples'
table_id = 'shakespeare'

dataset_ref = client.dataset(dataset_id, project=project)
table_ref = dataset_ref.table(table_id)
table = client.get_table(table_ref)


f = io.StringIO("")
client.schema_to_json(table.schema, f)
print(f.getvalue())
```

The output, 

```
[
  {
    "description": "A single unique word (where whitespace is the delimiter) extracted from a corpus.",
    "mode": "REQUIRED",
    "name": "word",
    "type": "STRING"
  },
  {
    "description": "The number of times this word appears in this corpus.",
    "mode": "REQUIRED",
    "name": "word_count",
    "type": "INTEGER"
  },
  {
    "description": "The work from which this word was extracted.",
    "mode": "REQUIRED",
    "name": "corpus",
    "type": "STRING"
  },
  {
    "description": "The year in which this corpus was published.",
    "mode": "REQUIRED",
    "name": "corpus_date",
    "type": "INTEGER"
  }
]

```
