[![CircleCI](https://circleci.com/gh/feedyard/circleci-remote-docker.svg?style=shield)](https://circleci.com/gh/feedyard/circleci-remote-docker)
[![Docker Repository on Quay](https://quay.io/repository/feedyard/circleci-remote-docker/status "Docker Repository on Quay")](https://quay.io/repository/feedyard/circleci-remote-docker)
# feedyard/circleci-remote-docker

Minimum docker image configuration, based on alpine linux, for use as a primary container in a circleci  
setup_remote_docker pipeline.  

See CHANGELOG for list of installed packages/versions  

## requirements for ci and local development

Environment variable FEEDYARD_PIPELINE_KEY used as encrypt/decrypt key for required secrets. Set matching var in  
circleci repository and include local file `local.env` with the following access information.  

```$xslt
FEEDYARD_CIRCLECI_QUAYIO_DEPLOY_USER=
FEEDYARD_CIRCLECI_QUAYIO_DEPLOY_USER_TOKEN=
```

run (or review) `prereqs.sh` to install requirements for local development.  
