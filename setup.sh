#!/bin/sh

# setup influx
sh Container_InfluxDB/run.sh

# setup grafana
sh Container_Grafana/run.sh

# setup webapp_one
sh Container_WebApp_One/build.sh
sh Container_WebApp_One/run.sh 1