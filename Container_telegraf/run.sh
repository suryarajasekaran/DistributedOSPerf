#!/bin/sh

docker run -d --name=telegraf --link influxdb:influxdb -p 8083:8083 -v /var/run/docker.sock:/var/run/docker.sock telegraf