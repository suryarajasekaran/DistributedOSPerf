import subprocess
import os

def scaleup(webapp_name):
    print "This is a scaleup program"
    output = subprocess.check_output(["docker", "ps", "--format", "\"{{.Names}}\"", "-f", "name="+webapp_name])
    output_list = output.split("\n")
    scale_number = len(output_list)
    subprocess.check_output(["sh", os.path.dirname(os.path.dirname(os.path.realpath(__file__)))+"/Container_"+webapp_name+"/run.sh", str(scale_number), str(8888 - scale_number + 1)])

def scaledown(webapp_name):
    print "This is a scaledown program"
    output = subprocess.check_output(["docker", "ps", "--format", "\"{{.Names}}\"", "-f", "name=" + webapp_name])
    output_list = output.split("\n")
    scale_number = len(output_list)
    if scale_number <= 0:
        subprocess.check_output(["sh", os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + "/Container_"+webapp_name+"/delete.sh",str(scale_number-1)])
