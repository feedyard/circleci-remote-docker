FROM alpine:3.9

LABEL maintainer=<nic.cheneweth@thoughtworks.com>

# packages required for use as a circleci remote-docker primary container
RUN apk update && \
    apk add --no-cache \
    git=2.20.1-r0 \
    openssh=7.9_p1-r4 \
    tar=1.32-r0 \
    gzip=1.10-r0 \
    ca-certificates=20190108-r0

HEALTHCHECK NONE
