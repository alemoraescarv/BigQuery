### FORMAT_DATE()

This function receives a DATE and retrieves a DATE with another fomart according to a [formatting string](https://cloud.google.com/bigquery/docs/reference/standard-sql/date_functions#supported_format_elements_for_date).

[Documentation](https://cloud.google.com/bigquery/docs/reference/standard-sql/date_functions#format_date).

```sql
SELECT *
FROM `test-proj-261014.sample.test_*` 
where _TABLE_SUFFIX = FORMAT_DATE('%Y%m%d', CURRENT_DATE)
```
Other example, 

```sql
with a as (
select '2019-01-01' as date union all 
select '2020-10-21' as date union all
select '2018-08-15' as date 
order by date
)
select  format_date("%Y-%W", cast(date as date)) as date_w,
        format_date("%Y-%V", cast(date as date)) as date_v 
from a
```
