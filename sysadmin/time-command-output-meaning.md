- Date : 2017-10-04
- Tags : #sysadmin #cpu #time

## TIME command output meaning

When you want to know how long does it take to run a process, just use `time` command as a prefix

```bash
$ time my_program arg1 arg2
real        0m0.003s
user        0m0.000s
sys         0m0.004s
```

- **real** : wall clock time, mean time to start to finish your process
- **user** : CPUs-time outside the kernel
- **sys** : CPUs-time within the kernel

**real+sys** result is total multi CPUs time (so if you have a multi core CPUs, it is often bigger than **real**)

