- Date : 2018-02-23
- Tags : #docker #devops

## Build lightweight image by using multistage

Docker is great tool to build a pull-n-run application. But sometime, your image will be large if you build image from a big base image which has compliling toolbox.

Ex:

**One-stage build**

```Dockerfile
FROM golang:1.9.2
WORKDIR /go/src/github.com/khanhicetea/test/
COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build .
ENTRYPOINT ["/go/src/github.com/khanhicetea/test/test"]
```

**Multi-stage builds**

```Dockerfile
FROM golang:1.9.2
WORKDIR /go/src/github.com/khanhicetea/test/
COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build .

FROM scratch
COPY --from=0 /go/src/github.com/khanhicetea/test/test .
ENTRYPOINT ["/test"]
```

So final image will only contains /test excutable file. `COPY --from=0` means COPY from build has index `0` in Dockerfile.

