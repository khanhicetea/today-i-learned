- Date : 2017-02-17
- Tags : #mysql #string #bug

## String problems can cause logical bugs in application

### Example table

```
mysql> describe `test`;
+------------+-------------+------+-----+-------------------+----------------+
| Field      | Type        | Null | Key | Default           | Extra          |
+------------+-------------+------+-----+-------------------+----------------+
| id         | smallint(6) | NO   | PRI | NULL              | auto_increment |
| name       | varchar(50) | NO   |     | NULL              |                |
| created_at | timestamp   | YES  | MUL | CURRENT_TIMESTAMP |                |
+------------+-------------+------+-----+-------------------+----------------+
3 rows in set (0.00 sec)
```

Here is dump file of the table


```sql
DROP TABLE IF EXISTS `test`;

CREATE TABLE `test` (
  `id` smallint(6) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `created_at` (`created_at`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

LOCK TABLES `test` WRITE;
/*!40000 ALTER TABLE `test` DISABLE KEYS */;

INSERT INTO `test` (`id`, `name`, `created_at`)
VALUES
	(1,'abc','2017-02-16 17:28:59'),
	(2,' ABC','2017-02-16 17:29:14'),
	(3,'ABC     ','2017-02-16 17:29:21'),
	(4,'aBc','2017-02-16 17:29:31');

/*!40000 ALTER TABLE `test` ENABLE KEYS */;
UNLOCK TABLES;
```

### Case Insensitive

When creating database, table and column, we have to set the default string **COLLATION** for them. And if we use collation end withs `_ci`, it means we ignore the Case Sensitive (or Case Insensitive).

Then `"abc" == "ABC"` or `"abc" == "aBc"` or `"abc" = "Abc"` or ... (`X = Y <=> UPPER(X) == UPPER(Y)`)

```
mysql> select ("abc" = "ABC") as `case1`, ("abc" = "aBc") as `case2`, ("abc" = "Abc") as `case3`, ("abc" = "abcd") as `wrong`;
+-------+-------+-------+-------+
| case1 | case2 | case3 | wrong |
+-------+-------+-------+-------+
|     1 |     1 |     1 |     0 |
+-------+-------+-------+-------+
1 row in set (0.00 sec)
```

### String Trimming

Check this out !

```
mysql> select `id`, CONCAT("'", `name`, "'") as `name_with_quote`, `created_at` from test;
+----+-----------------+---------------------+
| id | name_with_quote | created_at          |
+----+-----------------+---------------------+
|  1 | 'abc'           | 2017-02-16 17:28:59 |
|  2 | ' ABC'          | 2017-02-16 17:29:14 |
|  3 | 'ABC '          | 2017-02-16 17:29:21 |
|  4 | 'aBc'           | 2017-02-16 17:29:31 |
+----+-----------------+---------------------+
4 rows in set (0.00 sec)

mysql> select `id`, CONCAT("'", `name`, "'") as `name_with_quote`, `created_at` from test where `name` = 'abc';
+----+-----------------+---------------------+
| id | name_with_quote | created_at          |
+----+-----------------+---------------------+
|  1 | 'abc'           | 2017-02-16 17:28:59 |
|  3 | 'ABC '          | 2017-02-16 17:29:21 |
|  4 | 'aBc'           | 2017-02-16 17:29:31 |
+----+-----------------+---------------------+
3 rows in set (0.01 sec)

mysql> select `id`, CONCAT("'", `name`, "'") as `name_with_quote`, `created_at` from test where `name` = ' abc';
+----+-----------------+---------------------+
| id | name_with_quote | created_at          |
+----+-----------------+---------------------+
|  2 | ' ABC'          | 2017-02-16 17:29:14 |
+----+-----------------+---------------------+
1 row in set (0.00 sec)
```

BAAMMMMM !!! 

![holy-shit-the-illuminati-is-real](https://cloud.githubusercontent.com/assets/4528223/23033726/d15b7e76-f4ab-11e6-8525-46d3baeddc50.jpg)

MySQL do right trimming the string value before comparing.

So you must be becareful to trim value before storing to MySQL to make everything consistent.

### Storing Emoji in MySQL

Because Emoji use utf-8 4 bytes, so we must use the `utf8mb4` charset (utf8 multi-bytes 4).

It's safe when migrating charset from `utf8` to `utf8mb4` 😎 , but not the reverse way 😅
