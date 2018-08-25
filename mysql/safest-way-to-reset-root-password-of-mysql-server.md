- Date : 2018-08-25
- Tags : #mysql #sysadmin #database #security

## The safest way to reset root password of MySQL Server

When you get stucked in this error message **"Access denied for user 'root@localhost' ..."**, you search the way to reset the root password on the Internet, but life is Hard ! (No answer makes you feel it's right way, even some do not work)

So to solve this problem, we need to understand **MySQL Authentication**

**Step 1** : Disable **MySQL Authentication** by skip loading **grant-tables** on loading MySQL server

Open MySQL server config file, it might be in **/etc/mysql/mysql.conf.d/mysqld.cnf**. Add this line to section `mysql`

```
[mysqld]
skip-grant-tables
```

**DANGER : BE CAREFULL ! AFTER RESETTING SERVER, YOUR MYSQL SERVER ALLOWS ANY CONNECTION FROM ANY USER FROM ANY HOST BY ANY PASSWORD**

So safe way is to make sure that you are the only one connect MySQL, by 

- change to listening port of the server

```
[mysqld]
skip-grant-tables
port=6033
bind-address = 127.0.0.1
```

- disable access through MySQL socket

```bash
$ sudo chmod 400 /var/run/mysqld/mysqld.sock
```

**Step 2** : Restart the MySQL server

```bash
$ sudo systemctl restart mysql
```

**Step 3** : Connect to mysql server by mysql cli, now you can connect free

```bash
$ mysql -h 127.0.0.1 -P 6033
```

**Step 4** : Analyze mysql.user table

```sql
mysql> use mysql              
Database changed              
mysql> select Host, User, plugin, password_expired, account_locked from user where User = 'root';                                           
+-----------+------------------+-----------------------+------------------+----------------+
| Host      | User             | plugin                | password_expired | account_locked |
+-----------+------------------+-----------------------+------------------+----------------+
| %         | root             | mysql_native_password | N                | N              |
+-----------+------------------+-----------------------+------------------+----------------+
4 rows in set (0.00 sec)
```

These fields meaning :

- Host : allowed client host name or IP address
  - `127.0.0.1` : allow local clients connect via TCP
  - `localhost` : allow local clients connect via local UNIX socket file `/var/run/mysqld/mysqld.sock`
  - `%` : any wildcard, allow from all hosts
- User : allowed user name
  - `root` : allow root user
- plugin :
  - `mysql_native_password` : use hashing function of MySQL `PASSWORD('YOURPASSWORD')`, stored in `authentication_string` field (MySQL 5.7+) or `password` field (MySQL 5.6 or older)
  - `auth_socket` : use socket
- password_expired :
  - `Y` : password is expired
  - `N` : password is not expired (still working)
- account_locked :
  - `Y` : account is locked
  - `N` : account is not locked (still working)

**Step 5** : Reset your password

Rewrite your sql command by replacing `NEWPASSWORD` and **WHERE** statement to match account we analyze in Step 4

MySQL 5.7+

```sql
mysql> update user set plugin = 'mysql_native_password', authentication_string = PASSWORD('NEWPASSWORD'), password_expired = 'N', account_locked = 'N' where Host = '%' and User = 'root';
```

MySQL 5.6 or older

```sql
mysql> update user set plugin = 'mysql_native_password', password = PASSWORD('NEWPASSWORD'), password_expired = 'N', account_locked = 'N' where Host = '%' and User = 'root';
```

**Make sure that we changed 1 row by checking the result log : Query OK, 1 rows affected (0.00 sec)** 

**Step 6** : Flushing privileges

```sql
mysql> flush privileges;
mysql> quit;
```

**Step 7** : Rollback all config changes

Update your mysql server config file, make sure to comment out `skip-grant-tables`

```
[mysqld]
# skip-grant-tables
port=3306
bind-address = 127.0.0.1
```

```bash
$ sudo systemctl restart mysql
```
Trying to connect to MySQL server with your new password

```bash
$ mysql -u root -h 127.0.0.1 -p
```

If anything works perfectly, last step is enabling access to socket file

```bash
$ sudo chmod 777 /var/run/mysqld/mysqld.sock
```

HOPE IT HELP ! WE SOLVE PROBLEMS BY UNDERSTANDING IT !

