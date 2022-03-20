- Date : 2022-03-17
- Tags : #docker #security

## Becareful on using port mapping of Docker in Development

Many examples, articles and repository use insecure config in port mapping Docker.

This is example in official document of Docker

https://docs.docker.com/engine/reference/run/#detached--d

```bash
$ docker run -d -p 80:80 my_image nginx -g 'daemon off;'
```

or 

from 12.2k stars repo in Github

https://github.com/chatwoot/chatwoot/blob/develop/docker-compose.yaml#L89

```yml
    ports:
      - '5432:5432'
```

This mapping config means you will proxy all traffic from the container port to the docker host (your dev machine) with binding `0.0.0.0`. It means if you don't have a firewall or accidently open all ports, your contaier data will be public in the Local Network (so danger if you use in public places like coffee shops)

So remember to add the IP, which you wanted to bind in docker host (or have a network firewall ON)

```yml
    ports:
      - '127.0.0.1:5432:5432'
      - '172.17.0.1:5432:5432'
```

