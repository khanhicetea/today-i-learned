- Date : 2017-09-01
- Tags : #sysadmin #proxy #web

## Enable reverse proxy in CentOS

CentOS with SELinux enabled by default will block any http proxy connection. So you have to enable this permission.

Temporary enable

```bash
$ /usr/sbin/setsebool httpd_can_network_connect 1
```

Permanent enable

```bash
$ /usr/sbin/setsebool -P httpd_can_network_connect 1
```

