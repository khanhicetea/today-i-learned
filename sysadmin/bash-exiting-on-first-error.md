- Date : 2017-09-26
- Tags : #sysadmin #bash #shell

## BASH exiting on first error

Setting a flag `set -e` to bash script will let the script exit on first error occurs, so if you want to ignore a command just adding ` || true` to suffix

```bash
set -e

errorCmd $1 || true
echo "Run here !"
```

And opposite of `set -e` is `set +e`, haha of course !

```bash
set +e

errorCmd $1
echo "Still run here !"
```

