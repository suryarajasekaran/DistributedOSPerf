#!/bin/sh

docker stop $(docker ps -a -q --filter name="webapp_two_$1")
docker rm $(docker ps -a -q --filter name="webapp_two_$1")