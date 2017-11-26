from Monitor import webapp_monitor
import time
if __name__ == '__main__':
    while (True):
        webapp_monitor(webapp_name="webapp_one")
        time.sleep(10)

