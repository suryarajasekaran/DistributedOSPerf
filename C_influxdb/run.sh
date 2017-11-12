#!/bin/sh

docker run -d --name=influxdb -p 8086:8086 -v Container_InfluxDB:/var/lib/influxdb influxdb