- Date : 2017-09-01
- Tags : #sysadmin #ssh #security

## Create SSH tunnel manually

SSH Tunnel is a fast way to transfer traffic through unsafe internet today. It would be used in MySQL connect, FTP connect or HTTP connect, ...

Syntax :

```bash
$ ssh -L [local_port]:[remote_endpoint]:[remote_port] [ssh_user]:[ssh_ip]
```

Example :

Lets say you have a EC2 instance (123.45.67.89) and remote DB instance (98.76.54.32) listening port 3306

```bash
$ ssh -L 3307:98.76.54.32:3306 root@123.45.67.89
```

Testing ssh tunnel

```bash
$ telnet 127.0.0.1 3307
$ # or
$ mysql -h 127.0.0.1 -P 3307 -u root -p
```

