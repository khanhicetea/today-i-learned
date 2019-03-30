- Date : 2019-03-30
- Tags : #docker #root #linux

## Run container processes as non-root user

As default, docker runs your container as root user (uid=0). Although docker isolates your filesystem to protect docker host, but running processes as root is redundant and increasing attacking surface. Even it can make its written files having root owner, which can mess your docker-host filesystem permission.

This is example that show docker runs as root

```bash
$ docker run --rm alpine sleep 30
```

and open another terminal to check this

```bash
$ ps xau | grep 'sleep'
khanhic+ 15552  0.5  0.4 1264452 49280 pts/1   Sl+  17:37   0:00 docker run --rm alpine:3.9 sleep 30
root     15610  0.6  0.0   1520     4 ?        Ss   17:37   0:00 sleep 30
khanhic+ 15876  0.0  0.0  23076  1024 pts/2    S+   17:37   0:00 grep --color=auto sleep
```

You can see that the process **sleep 30** is running as root with pid = 15610

----

To control which user docker container runs as, you can use the `--user [userid]:[groupid]` argument

Example

```bash
$ docker run --rm --user 1000:1000 alpine sleep 30
```

Then you will get this result

```bash
$ ps xau | grep 'sleep'
khanhic+ 16275  2.0  0.4 1411916 50124 pts/1   Sl+  17:41   0:00 docker run --rm --user 1000:1000 alpine:3.9 sleep 30
khanhic+ 16336  1.5  0.0   1520     4 ?        Ss   17:41   0:00 sleep 30
khanhic+ 16403  0.0  0.0  23076   984 pts/2    S+   17:41   0:00 grep --color=auto sleep
```

**TIP** : you can set a environment variable by add this line to **~/.bash_profile** or **~/.bashrc**

```bash
export DOCKER_UID="$(id -u ${USER}):$(id -g ${USER})"`
```

then use docker command like `docker run --user $DOCKER_UID ....`

