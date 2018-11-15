- Date : 2018-11-15
- Tags : #linux #cron #bash

## Make cron job runs every seconds

Cron is a UNIX service that helps user run command periodically. And crontab is simple tool to setup cron job as user, just type in the command `crontab -e` then setup your cron schedule.

Btw, sometimes you want to run the cronjob every seconds (5, 10 or 20 seconds), but crontab only support every minute. How to achieve your goal without using another tool ?

I got an idea that we can use the `sleep` command to make it done. So this is solution.

This below is crontab rule that run command every 10 seconds.

```
* * * * * [command]
* * * * * sleep 10 && [command]
* * * * * sleep 20 && [command]
* * * * * sleep 30 && [command]
* * * * * sleep 40 && [command]
* * * * * sleep 50 && [command]
``` 

It's simple, right ? ;)

