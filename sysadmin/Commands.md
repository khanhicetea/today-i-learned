- Date : 2015-12-30
- Tags : #sysadmin #bash #command-line


## Commands

### Command `lsof`

List all opened files, sockets, pipes

Eg: 

- List processes are using port 80 (need root if port between 1-1023)

```bash
# sudo lsof -i:80
```

- List processes are using /bin/bash

```bash
# lsof /bin/bash
```

