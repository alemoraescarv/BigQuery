### Pandas DataFrame

[Documentation.](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_gbq.html)
 
Before running this Python script from the terminal, make sure the environment is properly set: 

```
pip install --upgrade google-cloud-bigquery
pip install --upgrade google-cloud-bigquery[pandas]
pip install --upgrade pandas_gbq
```

The module (pandas_gbq) is necessary because it is not included in the google-bigquery[pandas] package.

Syntax, 

```sql
import pandas as pd
from google.cloud import bigquery

records =[
    {
        "Name": "Alex",
        "Age": 25,
        "City":"New York"
    },
    {
        "Name": "Bryan",
        "Age": 27,
        "City":"San Francisco"

    }
]

dataframe = pd.DataFrame(
    records,columns=["Name","Age","City"])

print(dataframe)
