import time
import threading

start = time.perf_counter()

def do_something(n):
    print(f'This is the {n}th thread...')
    time.sleep(1)
    print('Done Sleeping')

threads = []    
for i in range(10):
    t = threading.Thread(target=do_something, args=(i,))
    t.start()
    threads.append(t)
    
for thread in threads:
    thread.join()
    
finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')