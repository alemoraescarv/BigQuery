### Maximum of bytes billed

[Documentation.](https://googleapis.dev/python/bigquery/latest/generated/google.cloud.bigquery.job.QueryJob.html)
The flag `max_bytes_billed` checks how many bytes it will be queried and just executes the query if it is within the quota.

Example of usage with pandas,

```python
from google.cloud import bigquery
import pandas

client = bigquery.Client()
dataset_ref = client.dataset("stackoverflow", project="bigquery-public-data")
dataset = client.get_dataset(dataset_ref)

job_config = bigquery.QueryJobConfig(maximum_bytes_billed=10**10)
job_config.use_query_cache = False

working_query = """
                SELECT a.id, a.body, a.owner_user_id
                FROM `bigquery-public-data.stackoverflow.posts_answers` AS a
                INNER JOIN `bigquery-public-data.stackoverflow.posts_questions` AS q
                    ON q.id = a.parent_id
                WHERE q.tags LIKE '%bigquery%'
                """
answers_query_job = client.query(working_query, job_config) 
answers_query_job.to_dataframe()
```
