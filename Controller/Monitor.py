import random
from Scale import scaleup, scaledown
import requests
from influxdb import InfluxDBClient

def webapp_monitor(webapp_name):
    if check_load(webapp_name=webapp_name) :
        scaleup(webapp_name)
    else:
        scaledown(webapp_name)

def check_load(webapp_name):
    if check_load_cpu(webapp_name) > 30:
        return True
    else:
        return False

def check_load_cpu(webapp_name):
    query = "SELECT mean(\"usage_percent\") FROM \"docker_container_cpu\" WHERE (\"container_name\" =~ /"+webapp_name+"*/) AND time > now() - 60s;"
    influxDBClient = InfluxDBClient('localhost', 8086, 'root', 'root', 'telegraf')
    result = influxDBClient.query(query)
    output = result.raw["series"][0]["values"][0][1]
    return output
