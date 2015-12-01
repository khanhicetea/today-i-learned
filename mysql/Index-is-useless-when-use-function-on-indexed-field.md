- Date : 2015-12-01
- Tags : #mysql #sql #index


## Index is useless when use function on indexed field

Reality, if using function on indexed field, you will broke indexing by accident.
Eg:

```sql
WHERE MONTH(`date`) = 11 AND YEAR(`date`) = 2015
```

Solution is transform the query to comparison query, like this :

```sql
WHERE `date` >= '2015-11-01' AND `date` < '2015-12-01'
```

