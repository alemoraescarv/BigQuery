### Inser into

*Stressing that, according to the documentation, if your table is partitioned you must include the columns names which will be used to insert new rows.*

[Documentation.](https://cloud.google.com/bigquery/docs/reference/standard-sql/dml-syntax#insert_statement)
Attention to omit a column name when nested,  [link.](https://cloud.google.com/bigquery/docs/reference/standard-sql/dml-syntax#omitting_column_names)

```sql
INSERT INTO `billing_bigquery` ( billing_account_id, service, sku, usage_start_time, usage_end_time, project, labels, system_labels, location, export_time, cost, currency, currency_conversion_rate, usage, credits  )#invoice, cost_type 
SELECT billing_account_id, service, sku, usage_start_time, usage_end_time, project, labels, system_labels, location, export_time, cost, currency, currency_conversion_rate, usage, credits 
FROM `billing_pubsub`
```
