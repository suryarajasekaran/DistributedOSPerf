#!/bin/sh

# setup influx
sh C_influxdb/run.sh

# setup database for metrics
curl -X POST 'http://localhost:8086/query?pretty=true'  --data-urlencode "q=CREATE DATABASE metrics"
# curl -G 'http://localhost:8086/query?pretty=true'  --data-urlencode "q=SHOW DATABASES"

# setup grafana
sh C_grafana/run.sh

# setup mongo
sh C_mongodb/run.sh

# setup webapp_one
sh C_webapp_one/build.sh
sh C_webapp_one/run.sh 1 8888