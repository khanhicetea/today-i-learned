- Date : 2018-01-22
- Tags : #sysadmin #logging

## Use journalctl to check system logs

Logging and Monitoring are important factor for system admin. Checking the log will help you have a closer look into the issue. One tool could help you will handy features is `journalctl`.

Here are simple options :
- `-f` : follow the log (tailf)
- `-u [service]` : filter to show only [service] logs
- `--since=[date]` : Show entries not older than the specified date
- `--until=[date]` : Show entries not newer than the specified date 

Example :

```bash
$ sudo journalctl -u nginx.service
$ sudo journalctl -u nginx.service --since yesterday
$ sudo journalctl -u nginx.service --since "2018-01-01" --until today
```

