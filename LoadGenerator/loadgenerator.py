from Load import parallel_induce_load_endpoint
from multiprocessing import Process
import time

if __name__ == '__main__':
    try:
        while (True):

            p_list = []

            p = Process(target=parallel_induce_load_endpoint, args=("webapp_one", 30))
            p.start()
            p_list.append(p)

            #p = Process(target=parallel_induce_load_endpoint, args=("webapp_two", 30))
            #p.start()
            #p_list.append(p)

            #p = Process(target=parallel_induce_load_endpoint, args=("webapp_three", 30))
            #p.start()
            #p_list.append(p)

            #p = Process(target=parallel_induce_load_endpoint, args=("webapp_four", 30))
            #p.start()
            #p_list.append(p)

            for p in p_list:
                p.join()
    except KeyboardInterrupt:
        print('Stopping Load')


