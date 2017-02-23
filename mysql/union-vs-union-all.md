- Date : 2017-02-23
- Tags : #mysql #database

## UNION vs UNION ALL

The difference is UNION command will sort and remove duplicated rows (RETURNED ONLY DISTINCT ROWS)

Examples :

```sql
mysql> select '1', '2' union select '2', '1' union select '3', '4' union select '1', '2';
+---+---+
| 1 | 2 |
+---+---+
| 1 | 2 |
| 2 | 1 |
| 3 | 4 |
+---+---+
3 rows in set (0.00 sec)

mysql> select '1', '2' union select '2', '1' union select '3', '4' union select '1', '3';
+---+---+
| 1 | 2 |
+---+---+
| 1 | 2 |
| 2 | 1 |
| 3 | 4 |
| 1 | 3 |
+---+---+
4 rows in set (0.00 sec)

mysql> select '1', '2' union all select '2', '1' union all select '3', '4' union all select '1', '2';
+---+---+
| 1 | 2 |
+---+---+
| 1 | 2 |
| 2 | 1 |
| 3 | 4 |
| 1 | 2 |
+---+---+
4 rows in set (0.00 sec)
```

**Tips**

In case there will be no duplicates, using UNION ALL will tell the server to skip that (useless, expensive) step.

