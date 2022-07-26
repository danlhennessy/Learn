import time
import multiprocessing

#Threads share global variables. By contrast, separate processes are completely separate; one process cannot affect another's variables

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} sec...')
    time.sleep(seconds)
    print('Done Sleeping')
    
p1 = multiprocessing.Process(target=do_something)
p2 = multiprocessing.Process(target=do_something)

if __name__ == '__main__':
    processes = []
    for v in range(10):
        p = multiprocessing.Process(target=do_something, args=(1.5,)) #  Args must be able to be serialised using pickle. Tuple is recommended
        p.start()
        processes.append(p)
        
    for process in processes:
        process.join()
        
    finish = time.perf_counter()

    print(f'Finished in {round(finish - start, 2)} second(s)')