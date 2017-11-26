import random
from Scale import scaleup, scaledown

def webapp_monitor(webapp_name):
    if check_load(webapp_name=webapp_name) :
        scaleup(webapp_name)
    else:
        scaledown(webapp_name)

def check_load(webapp_name):
    output=True#random.choice([True, False])
    #TODO : OUTPUT wiring with infux DB
    return output
