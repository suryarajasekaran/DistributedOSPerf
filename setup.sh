#!/bin/sh

# setup influx
sh Container_influxdb/run.sh

# setup database for metrics
sleep 5 # sleep for 5secs before attempting to create a database on influx
curl -X POST 'http://localhost:8086/query?pretty=true'  --data-urlencode "q=CREATE DATABASE telegraf"
# curl -G 'http://localhost:8086/query?pretty=true'  --data-urlencode "q=SHOW DATABASES"
#ALTER RETENTION POLICY autogen ON telegraf DURATION 6h SHARD DURATION 1h
# setup grafana
sh Container_grafana/run.sh

# setup mongo
sh Container_mongodb/run.sh

# setup webapp_one
sh Container_webapp_one/build.sh
sh Container_webapp_one/run.sh 1 8888