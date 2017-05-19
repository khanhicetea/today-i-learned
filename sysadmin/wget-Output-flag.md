- Date : 2017-05-19
- Tags : #sysadmin #shell

## wget Output flag

`-O` means output

```bash
$ # output file will be index.html or based on header filename
$ wget -O www.abc.xyz
```

```bash
$ # output file will be filename.html
$ wget -O filename.html www.abc.xyz
```

```bash
$ # output to stdout
$ wget -O- www.abc.xyz
$ wget -O- https://gist.githubusercontent.com/khanhicetea/4fa9f5103cd7fbc2d2270abce05c9c2b/raw/helloworld.sh | bash
```

