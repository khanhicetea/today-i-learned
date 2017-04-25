- Date : 2017-04-25
- Tags : #database #sqlite

## Basics about sqlite command line tool

We can use `sqlite3` command line tool to run SQL statement in sqlite3 file.

### View all table : `.tables`
### Truncate table : `delete from [table_name];` then run `vacuum;` to clear space
### Close : press `Ctrl ^ D` to escape

```bash
$ sqlite3 database.sqlite
SQLite version 3.8.10.2 2015-05-20 18:17:19
Enter ".help" for usage hints.
sqlite> .tables
auth_group                  backend_church
auth_group_permissions      backend_masstime
auth_permission             django_admin_log
auth_user                   django_content_type
auth_user_groups            django_migrations
auth_user_user_permissions  django_session
backend_area
sqlite> select * from auth_user;
1|pbkdf2_sha256$30000$QQSOJMiXmNly$mWUlYwZnaQGsv9UVZcdTb29P7IHrgnd7ja3T/uwFqvw=|2017-03-25 15:06:40.528549|1|||hi@khanhicetea.com|1|1|2017-03-25 15:06:23.822489|admin
sqlite> describe auth_user;
Error: near "describe": syntax error
sqlite> select * from django_session;
4nmyjqpw292bmdnb5oxasi74v9rdhzoc|MzcwZDMxMzk5MGZkZTg2MjY4YWYyNmZiMzRkNWQwOTVjYzczODk5OTp7Il9hdXRoX3VzZXJfaGFzaCI6IjhlZTZjM2NhOGJjNWU4ODU0ZGE3NTYzYmQ4M2FkYzA0MGI4NTI4NzgiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=|2017-04-08 15:06:40.530786
sqlite> delete from django_session;
sqlite> vacuum;
sqlite> ^D
```

