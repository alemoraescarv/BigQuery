### Converting a simple JSON to New Line Delimited JSON file.

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
