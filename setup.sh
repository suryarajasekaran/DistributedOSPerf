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

# setup webapp_two
sh Container_webapp_two/build.sh
sh Container_webapp_two/run.sh 1 7777

# setup webapp_two
sh Container_webapp_three/build.sh
sh Container_webapp_three/run.sh 1 6666

# setup webapp_two
sh Container_webapp_four/build.sh
sh Container_webapp_four/run.sh 1 5555