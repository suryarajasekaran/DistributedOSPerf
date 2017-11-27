#!/bin/sh

docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
docker rmi $(docker images ps -a)
docker volume rm $(docker volume ls -qf dangling=true)

