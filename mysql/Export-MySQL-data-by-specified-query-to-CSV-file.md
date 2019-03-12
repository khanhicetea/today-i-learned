- Date : 2019-03-12
- Tags : #mysql #cli

## Export MySQL data by specified query to CSV file

To export data from MySQL by specified query to CSV file, you can use this command

```bash
$ mysql -B -u username -p database_name -h dbhost -e "SELECT * FROM table_name;" | sed "s/'/\'/;s/\t/\",\"/g;s/^/\"/;s/$/\"/;s/\n//g"
```

Tip from : https://stackoverflow.com/a/25427665

