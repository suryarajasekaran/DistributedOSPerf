from Load import parallel_induce_load_endpoint
import time

if __name__ == '__main__':
    try:
        while (True):
            parallel_induce_load_endpoint(webapp_name="webapp_one", load_parallel=30)
            parallel_induce_load_endpoint(webapp_name="webapp_two", load_parallel=30)
            parallel_induce_load_endpoint(webapp_name="webapp_three", load_parallel=30)
            parallel_induce_load_endpoint(webapp_name="webapp_four", load_parallel=30)
    except KeyboardInterrupt:
        print('Stopping Load')


