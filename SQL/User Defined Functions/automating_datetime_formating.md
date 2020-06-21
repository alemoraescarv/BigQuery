### Formating DATETIME

In order to automate the DATE formating and making the code reusable using UDF in BigQuery. 

Below is the code and output, 

```python
#extracting the timestamp
CREATE TEMP FUNCTION
  datetime_func (s string)
  RETURNS string
  LANGUAGE js AS '''

  var myRe =  new RegExp(/\\[.*\\]/,'g');
  date_str =s.replace(myRe,"");
  return [(date_str)];
''';

#checking if the timestamp has seconds or not
CREATE TEMP FUNCTION
  format_check (s string)
  RETURNS BOOLEAN
  LANGUAGE js AS '''

  if(s.length == 25){ 
  //if the date string has the seconds with 2 digits
    return true;
  }else {return false;}
''';

CREATE TEMP FUNCTION
  get_timezone (s string)
  RETURNS string
  LANGUAGE js AS '''

  var myre = new RegExp(/\\[.*\\]/);
  z = (s.match(/\\[(.*?)\\]/));
  return z[1];
''';

#extracting the date
CREATE TEMP FUNCTION
  date_func (s string)
  RETURNS string
  LANGUAGE js AS '''
  return s.slice(0,10);
''';


WITH data AS (
  SELECT '2015-09-02T10:44+02:00[Europe/Berlin]' time_data UNION ALL
  SELECT '2015-08-22T14:17:36+02:00[Europe/Oslo]' UNION ALL
  SELECT '2020-05-08T15:00+02:00[Europe/Madrid]' 
)
SELECT time_data as ts
        #getting the date and converting to date format
        ,PARSE_DATE('%Y-%m-%d',date_func(time_data)) as date

       #if true, format with seconds and formating as timestamp format
        ,IF(format_check(datetime_func(time_data)) = True,
         (PARSE_TIMESTAMP('%Y-%m-%dT%H:%M:%S%Ez',datetime_func(time_data))), 
         (PARSE_TIMESTAMP('%Y-%m-%dT%H:%M%Ez', datetime_func(time_data)))) as timestamp, 
         get_timezone(time_data) as zone

FROM data
```


And the output: 

[![enter image description here][2]][2]

Notice in the code that it was necessary to convert the date and the timestamp from *String* to *DATE* and *TIMESTAMP*, respectively. 

  [1]: https://cloud.google.com/bigquery/docs/reference/standard-sql/user-defined-functions
  [2]: https://i.stack.imgur.com/tN5kB.png
  [3]: https://cloud.google.com/bigquery/docs/writing-results#writing_query_results
  [4]: https://i.stack.imgur.com/z7bRE.png

