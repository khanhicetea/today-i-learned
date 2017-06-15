- Date : 2017-06-15
- Tags : #sysadmin #gearman #queue

## Gearman bash worker and client

Gearman is a awesome job queue service that helps you scale your system. In smaller context, it can help us to run a background woker for minor tasks like backup data, cleaning system.

**Install** :

```bash
$ sudo apt install gearman-job-server gearman-tools
```

**Create a worker bash script**

worker.sh

```bash
#!/bin/bash

echo $1
echo $2
```

**Run worker**, `-w` means run as worker mode , `-f test` means function name will be `test`

```bash
$ chmod +x worker.sh
$ gearman -w -f test xargs ./worker.sh
```

**Sending job**

```bash
$ gearman -f test "hello" "hogehoge"
```

**Sending background job**

```bash
$ gearman -b -f test "hello" "hogehoge"
```

