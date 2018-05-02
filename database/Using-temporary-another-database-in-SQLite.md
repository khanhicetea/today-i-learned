- Date : 2018-05-02
- Tags : #database #sqlite

## Use temporarily data from another database in SQLite

Sometimes, we need to use temporarily data from another database file. There is simple and fast way to achieve that without transfering data from file X to file Y.

We connect to main database

```bash
$ sqlite3 main.sqlite
```

Then using the **ATTACH** command to attach another database as an alias in main database

```
> ATTACH another_db.sqlite as TEMP;
```

Let listing the tables

```
> .tables
TEMP.users
TEMP.posts
users
admins
categories
```

As you can see, we got a list of tables, which are prefixed by defined alias `TEMP` we used in ATTACH command. So you only need to use these tables as normal tables.

Example of copying data between 2 tables (same structure) :

```
> INSERT INTO users SELECT * FROM TEMP.users;
```

