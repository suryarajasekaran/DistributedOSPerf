#!/bin/sh

# setup influx
sh Container_influxdb/run.sh

# setup telegraf
sh Container_telegraf/run.sh

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

# setup webapp_three
sh Container_webapp_three/build.sh
sh Container_webapp_three/run.sh 1 9999

# setup webapp_four
sh Container_webapp_four/build.sh
sh Container_webapp_four/run.sh 1 5555

# source venv
source venv.sh