- Date : 2018-05-29
- Tags : #git #secutiry

## Put .git data outside project directory

Sometimes you want to put .git data into outside directory (to use another disk partition or to protect your git data). Use `--separate-git-dir=` option to get that.

Example :

```bash
$ git init --separate-git-dir=/var/gitstorage/myproject
```

Bonus : to protect .git data from other users, use this option `--shared` within octal value (same to `chmod`)

Example : this will protect git file from writing by group and reading/writing by others

```bash
$ git init --separate-git-dir=/var/gitstorage/myproject --shared=0640
```

