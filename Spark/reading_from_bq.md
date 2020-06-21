### Spark job to read from BigQuery

According to the [PySpark documentation][2], in the *class pyspark.sql.DataFrameWriter(df)*, there is an option called ***nullValue***:

> **nullValue** – sets the string representation of a null value. If None is
> set, it uses the default value, empty string.


Which is what you are looking for. Then, I just implemented nullValue option below.

```python
sc = SparkContext()
spark = SparkSession(sc)

# Read the data from BigQuery as a Spark Dataframe.
data = spark.read.format("bigquery").option(
    "table", "dataset.table").load()

# Create a view so that Spark SQL queries can be run against the data.
data.createOrReplaceTempView("data_view")

# Select required data into another df
data_view2 = spark.sql(
    'SELECT * FROM data_view')

df=data_view2.write.csv('gs://bucket/folder', header=True, nullValue='')

data_view2.show()
```
