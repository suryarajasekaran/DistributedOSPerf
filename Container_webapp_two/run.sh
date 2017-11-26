#!/bin/sh

docker run -d --name="webapp_two_$1" --link influxdb:influxdb --link mongodb:mongodb -p "$2":7777 -m 50m webapp_two