- Date : 2018-04-10
- Tags : #sysadmin #trick #networking

## Send a file through networking via netcat

If you're working on 2 machines in same networking and want to send a file from machine A to machine B. But you don't have USB, floopy disk :lol: or insanse Bluetooth. There is simple way to send a file to another computer without setting up SSH or SMB (althrough these way are safer than it).

On the machine A (with IP address : 192.168.1.2)

```bash
$ cat data.txt | sudo nc -l 0.0.0.0 6666
```

On the machine B

```bash
$ nc 192.168.1.2 6666 > here_the_data.txt
```

Have fun playing net😼 !! ;)

