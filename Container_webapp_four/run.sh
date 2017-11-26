#!/bin/sh

docker run -d --name="webapp_four_$1" --link influxdb:influxdb --link mongodb:mongodb -p "$2":5555 -m 50m webapp_four