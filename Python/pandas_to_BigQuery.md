### Pandas dataframe to BigQuery

[Documentation.](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_gbq.html)
 
Before running this Python script from the terminal, make sure the environment is properly set: 

```
pip install --upgrade google-cloud-bigquery
pip install --upgrade google-cloud-bigquery[pandas]
pip install --upgrade pandas_gbq
```
One of the ways of using `to_gbq` method is below,

```python
from google.cloud import bigquery 
import pandas as pd


table_schema = [{'name':'my_datetime', 'type':'DATE'},{'name':'my_string', 'type':'string'}]
df = pd.DataFrame(
    {
        "my_datetime": ["2020-01-01", "2020-01-01", "2020-01-01"],
        "my_string": ['a1',None, 'a3'],
    }
)

df.to_gbq(destination_table='data_frame.data_set', project_id='project_id', if_exists='replace')
```

