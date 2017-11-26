import subprocess
import os
from multiprocessing import Process
import requests
from random import randint

webapp_port_mapper_dict = {
                                "webapp_one"    : 8888,
                                "webapp_two"    : 7777,
                                "webapp_three"  : 6666,
                                "webapp_four"   : 5555
                          }

def induce_load_endpoint(wepapp_port):
    print "This is a induce load program"
    requests.get("http://0.0.0.0:"+str(wepapp_port)+"/test")


def parallel_induce_load_endpoint(webapp_name, load_parallel):
    output = subprocess.check_output(["docker", "ps", "--format", "\"{{.Names}}\"", "-f", "name=" + webapp_name])
    output_list = output.split("\n")
    scale_number = len(output_list) - 1
    p_list = []
    for i in range(0, load_parallel):
        p = Process(target=induce_load_endpoint, args=(randint(webapp_port_mapper_dict[webapp_name] - scale_number + 1, webapp_port_mapper_dict[webapp_name]),))
        p.start()
    for p in p_list:
        p.join()


def induce_load_browser(webapp_name, webapp_port):
    print "This is a induce load program"
    output = subprocess.check_output(["open", "http://0.0.0.0:"+str(webapp_port)+"/test"])


def parallel_induce_load_browser(webapp_name, webapp_port, load_parallel):
    p_list = []
    for i in range(0, load_parallel):
        p = Process(target=induce_load_browser, args=(webapp_name, webapp_port))
        p.start()
    for p in p_list:
        p.join()




