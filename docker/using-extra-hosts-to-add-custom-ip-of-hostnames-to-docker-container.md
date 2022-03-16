- Date : 2022-03-16
- Tags : #docker #networking

## Using extra hosts to add custom ip of hostnames to Docker container

By default, all docker container using DNS server from docker host, so if you want to overwrite the specific hostnames ip address, try the flag `--add-host [hostname]:[ip]`

```bash
$ docker run -it --add-host db1:1.2.3.4 --add-host db2:2.3.4.5 alpine cat /etc/hosts
127.0.0.1       localhost
::1     localhost ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
1.2.3.4 db1
2.3.4.5 db2
172.17.0.2      0bdcf2fb2216
```

If you use **docker-compose**, then add the extra-hosts param below the service you want

```yml
    extra_hosts:
      - "crm.dev:host-gateway"
      - "db1:1.2.3.4"
```

Bonus : `host-gateway` mean the ip address of the gateway of network container in, often be the docker host!

