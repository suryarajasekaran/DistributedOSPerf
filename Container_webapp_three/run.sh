#!/bin/sh

docker run -d --name="webapp_three_$1" --link influxdb:influxdb --link mongodb:mongodb -p "$2":9999 -m 50m webapp_three