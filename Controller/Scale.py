import subprocess
import os

webapp_port_mapper_dict = {
                                "webapp_one"    : 8888,
                                "webapp_two"    : 7777,
                                "webapp_three"  : 9999,
                                "webapp_four"   : 5555
                          }

def scaleup(webapp_name):
    print "This is a scaleup for "+str(webapp_name)
    output = subprocess.check_output(["docker", "ps", "--format", "\"{{.Names}}\"", "-f", "name="+webapp_name])
    output_list = output.split("\n")
    scale_number = len(output_list)
    subprocess.check_output(["sh", os.path.dirname(os.path.dirname(os.path.realpath(__file__))) +"/Container_" + webapp_name +"/run.sh", str(scale_number), str(webapp_port_mapper_dict[webapp_name] - scale_number + 1)])


def scaledown(webapp_name):
    output = subprocess.check_output(["docker", "ps", "--format", "\"{{.Names}}\"", "-f", "name=" + webapp_name])
    output_list = output.split("\n")
    scale_number = len(output_list)
    if scale_number > 2:
        print "This is a scaledown for " + str(webapp_name)
        subprocess.check_output(["sh", os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + "/Container_"+webapp_name+"/delete.sh", str(scale_number-1)])