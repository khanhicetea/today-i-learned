- Date : 2016-03-26
- Tags : #sysadmin #bash #command-line


## Stats your top-10 frequently commands

Run this command, it will show top-10 frequently commands, [explain shell](http://explainshell.com/explain?cmd=history+%7C+awk+%27%7Bprint+%242%7D%27+%7C+sort+%7C+uniq+-c+%7C+sort+-nr+%7C+head)

```bash
$ history | awk '{print $2}' | sort | uniq -c | sort -nr | head
```

Example result

```
2064 git
1284 ls
 826 cd
 700 ssh
 602 clear
 491 python
 473 exit
 341 vagrant
 242 export
 167 ping
```
