- Date : 2017-05-17
- Tags : #sysadmin #compressing #rar

## Compressing and Extracting files with rar and unrar in Linux

### zip and tar disadvantages

**All unicode filename will be transform to weird character, so it makes broken paths and broken links**

### Installation

Ubuntu :

```shell
$ sudo apt install rar unrar
```

Redhat ( using [RPMForge](http://repoforge.org/use/) )

```shell
$ sudo yum install rar unrar
```

### Compressing files, folder

Compressing files

```shell
$ rar a result.rar file1 file2 file3 fileN
```

Compressing dir and its subdirs (remember with trailing slash in the end)

```shell
$ rar a -r result.rar folder1/
```

Locking RAR file with password (adding `-p"THE_PASSWORD_YOU_WANT"`)

```shell
$ rar a -p"0cOP@55w0rD" result.rar file1 file2 file3 fileN
$ rar a -p"0cOP@55w0rD" -r result.rar folder1/
```


### Extracting file

Listing content of RAR file

```shell
$ unrar l result.rar
```

Extracting RAR file to current dir

```shell
$ unrar e result.rar
```

Extracting RAR file to current dir with fullpath

```shell
$ unrar x result.rar
```

### WANT MORE ?

Asking itself !

```shell
$ rar -?
$ unrar -?
```

### BONUS

> WHAT IF I TOLD U THAT A RAR FILE BIGGER 35 TIMES THAN ITS ORIGINAL FILE ?

```shell
$  echo 'a' > a.txt
$  rar a a.rar a.txt

RAR 3.80   Copyright (c) 1993-2008 Alexander Roshal   16 Sep 2008
Shareware version         Type RAR -? for help

Evaluation copy. Please register.

Creating archive a.rar

Adding    a.txt                                                       OK 
Done
$  ls -al
total 72
-rw-r--r-- 1 root root    77 May 17 14:18 a.rar
-rw-r--r-- 1 root root     2 May 17 14:17 a.txt
```

![bus rar](https://cloud.githubusercontent.com/assets/4528223/26142566/44a8d4f0-3b0b-11e7-8f03-271fd1326215.jpg)

