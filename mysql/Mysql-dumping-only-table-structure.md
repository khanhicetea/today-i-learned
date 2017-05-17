- Date : 2017-05-17
- Tags : #mysql

## Mysql dumping only table structure

Adding `-D` to dump only data structureA

Example :

```shell
$ mysqldump -h 127.0.0.1 -u root -p"something" -D database1 > db.sql
```

