# how to nulk delete tables in BigQuery using Python API

import datetime
import os

client = bigquery.Client()
dataset_id = 'your-project.your_dataset'
tables = client.list_tables(dataset_id)

begin = datetime.date(2019,6,1)
end = datetime.date(2019,6,7)

for table in tables:
        print("{}.{}.{}".format(table.project, table.dataset_id, table.table_id))
        for i in range((end - begin).days+1):
            day = begin + datetime.timedelta(days=i)
            os.system("bq rm -f -t 'DATASET.TABLENAME$day'") 
