### Uploading multiple .csv files to BigQuery. 

Below is the script, 

```bash
echo "Starting the script"
for i in *.csv;
do
        echo ${i%.csv} " loading";
        bq load --autodetect --source_format=CSV project_id:dataset.Table_${i%.csv} ./$i;
        echo ${i%.csv} " was loaded"
done
```

Notice that the table schema is being automatically detected.
