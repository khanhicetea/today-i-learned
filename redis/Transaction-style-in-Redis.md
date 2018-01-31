- Date : 2018-01-31
- Tags : #redis #transaction

## Transaction style in Redis

In Redis, you can use transaction-style (mean queue commands then flush it once). It will improve performance in many case where latency or networking is slow.

```
> SET hoge 2
OK
> MULTI
OK
> INCR foo
QUEUED
> INCR hoge
QUEUED
> EXEC
1) (integer) 1
2) (integer) 1
```

`MULTI` command is **begin transaction** and `EXEC` command is **commit transaction**

The result will be returned in order your command queue list.

