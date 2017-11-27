from Monitor import webapp_monitor
import time
if __name__ == '__main__':
    while(True):
        webapp_monitor(webapp_name="webapp_one")
        webapp_monitor(webapp_name="webapp_two")
        webapp_monitor(webapp_name="webapp_three")
        webapp_monitor(webapp_name="webapp_four")
        time.sleep(10)

