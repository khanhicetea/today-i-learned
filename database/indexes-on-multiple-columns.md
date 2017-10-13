- Date : 2017-10-13
- Tags : #database #indexes

## Indexes on multiple columns

Let's say you have an indexes on 2 columns (A, B) of the table (X). So this is three use cases happen :

1. You query data based on both of 2 columns => Indexes will be considered
2. You query data based on (A) => Indexes will be considered
3. You query data based on (B) => Indexes will be ignored because database indexes your data by B-tree algo. So it can't search node via a B => If you want, just create another indexes on B column

I said `will be considered` because it depends on your query and your data (query optimizer will decide it !)

