#!/bin/sh

docker run -d --name="webapp_one_$1" -p 8888:8888 webapp_one