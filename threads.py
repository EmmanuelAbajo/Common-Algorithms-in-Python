import os
import threading as th

def cpu_waster():
    while True:
        pass

def display_thread_info():
    print(f'Process ID: {os.getpid()}')
    print(f'Thread count: {th.active_count()}')
    for thread in th.enumerate():
        print(thread)

display_thread_info()
print('Starting waster threads')
for i in range(5):
    th.Thread(target=cpu_waster).start()
display_thread_info()    