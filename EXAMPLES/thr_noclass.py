#!/usr/bin/env python

import threading
import random
import time

data_lock = threading.Lock()

data = {}

def doit(num):  # , next_function):  # <1>
    time.sleep(random.randint(1, 3))
    print("Hello from thread {}".format(num))
    with data_lock: # waits for, then acquires lock
        data[num] = "DONE"
        # releases lock
    # t = threading.Thread(target=next_function)
    # t.start()


t_list = []
for i in range(10):
    t = threading.Thread(target=doit, args=(i,))  # <2>
    t.start()  # <3>
    t_list.append(t)

print("All threads launched.")
print(t_list)
print(list(threading.enumerate()))


while True:
    for t in t_list:
        if not t.isAlive():
            #  do something with result and launch next or whatever
            pass #
    time.sleep(.5)

