import subprocess
import os

webapp_port_mapper_dict = {
                                "webapp_one"    : 8888,
                                "webapp_two"    : 7777,
                                "webapp_three"  : 6666,
                                "webapp_four"   : 5555
                          }

def scaleup(webapp_name):
    print "This is a scaleup program"
    output = subprocess.check_output(["docker", "ps", "--format", "\"{{.Names}}\"", "-f", "name="+webapp_name])
    output_list = output.split("\n")
    scale_number = len(output_list)
    subprocess.check_output(["sh", os.path.dirname(os.path.dirname(os.path.realpath(__file__))) +"/Container_" + webapp_name +"/run.sh", str(scale_number), str(webapp_port_mapper_dict[webapp_name] - scale_number + 1)])


def scaledown(webapp_name):
    print "This is a scaledown program"
    output = subprocess.check_output(["docker", "ps", "--format", "\"{{.Names}}\"", "-f", "name=" + webapp_name])
    output_list = output.split("\n")
    scale_number = len(output_list)
    if scale_number <= 0:
        subprocess.check_output(["sh", os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + "/Container_"+webapp_name+"/delete.sh", str(scale_number-1)])