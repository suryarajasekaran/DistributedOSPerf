#!/bin/sh

docker stop $(docker ps -a -q --filter name="webapp_three_$1")
docker rm $(docker ps -a -q --filter name="webapp_three_$1")