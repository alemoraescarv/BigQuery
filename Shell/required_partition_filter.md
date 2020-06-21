### Require partition filter

There are various of flags within this command, including require_partition_filter and norequire_partition_filter, in order to set the partition filter to True or False, respectively.

The syntax is below, 

```
bq update --norequire_partition_filter --time_partitioning_field=your_partition_field project:dataset.table
```
