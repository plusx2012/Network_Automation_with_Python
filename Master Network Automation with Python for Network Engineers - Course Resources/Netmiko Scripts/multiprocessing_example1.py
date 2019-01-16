import multiprocessing as mp
import time

def print_name_and_time(name):
    print('Hello ', name, ' current timestamp is ', time.time())
    print('Sleeping for 5 seconds...')
    time.sleep(5)
    print('After sleeping...')


if __name__ == '__main__':
    process_list = list()

    for i in range(10):
        process = mp.Process(target=print_name_and_time, args=('Andrei',))
        process_list.append(process)


    for p in process_list:
        p.start()


    for p in process_list:
        p.join()