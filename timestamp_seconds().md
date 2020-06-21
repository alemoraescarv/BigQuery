### TIMESTAMP_SECONDS()

This function converts seconds to DATETIME format. This syntax is below:\


```sql
WITH table_newStruct as(
  SELECT 
#Select all the desired fields
         searchDocId,
         STRUCT(TIMESTAMP_SECONDS(daySliderTimes._field_1.seconds) as startTime, 
         TIMESTAMP_SECONDS(daySliderTimes._field_.seconds) as endTime) as new_daySlidertimes

FROM 'table_source')

SELECT searchDocId, new_daySlidertimes 
FROM 'table_newStruct'
```
