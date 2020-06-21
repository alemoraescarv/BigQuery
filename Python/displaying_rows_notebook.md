### Setting the number of rows to be displayed

In a Python notebook, in order to set the number of rows which will be displayed after executing a query can be set as follows: 

 1. Setting to 300 rows
 
```python
import pandas as pd 
pd.set_option('display.max_rows', 3000)
```

 2. Setting the number of displayed rows to unlimited
 
 ```python 
 import pandas as pd
 pd.set_option('display.max_rows', None)
 ```
 
