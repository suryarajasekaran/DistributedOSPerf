#!/bin/sh

# setup influx
sh Container_influxdb/run.sh

# setup database for metrics
curl -X POST 'http://localhost:8086/query?pretty=true'  --data-urlencode "q=CREATE DATABASE metrics"
# curl -G 'http://localhost:8086/query?pretty=true'  --data-urlencode "q=SHOW DATABASES"

# setup grafana
sh Container_grafana/run.sh

# setup mongo
sh Container_mongodb/run.sh

# setup webapp_one
sh Container_webapp_one/build.sh
sh Container_webapp_one/run.sh 1 8888