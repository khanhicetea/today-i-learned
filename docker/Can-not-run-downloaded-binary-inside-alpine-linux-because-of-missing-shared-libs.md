- Date : 2019-02-02
- Tags : #docker #alpine #ldd

## Can not run downloaded binary inside alpine linux because of missing shared libs

Alpine linux becomes the most base image for docker images because it's lightweight and handful package manager **apk**. Sometimes, you create an image that downloads the binary file but can not execute it. It shows something like this:

```
/entrypoint.sh: line ***: [your binary]: not found
```

The problem is your binary built within shared libraries, so it can't run without shared libraries dependencies. To findout which libraries is missing, use this

```bash
$ ldd [your binary path]
```

This is sample result

```
/usr/local/bin # ldd hugo
        /lib64/ld-linux-x86-64.so.2 (0x7fa852f2a000)
        libpthread.so.0 => /lib64/ld-linux-x86-64.so.2 (0x7fa852f2a000)
Error loading shared library libstdc++.so.6: No such file or directory (needed by hugo)
        libdl.so.2 => /lib64/ld-linux-x86-64.so.2 (0x7fa852f2a000)
        libm.so.6 => /lib64/ld-linux-x86-64.so.2 (0x7fa852f2a000)
Error loading shared library libgcc_s.so.1: No such file or directory (needed by hugo)
        libc.so.6 => /lib64/ld-linux-x86-64.so.2 (0x7fa852f2a000)
```

So we need to install `libstdc++` and `libc6-compat` before run the binary

```
RUN apk add --no-cache libstdc++ libc6-compat
```

