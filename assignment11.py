#Q1.  Create a threading process such that it sleeps for 5 seconds and then prints out a message.
import thread
import time

def time(name,delay):
    count = 0
    while count<5:
        time.sleep(5)
        count += 1
        print('%s,%s' % (name,time.ctime(time.time)))

try:
    thread.start_new_thread (time,('thread-1',2))
    thread.start_new_thread (time,('thread-1',4))
except:
    print("unable to start")
while True:
    pass

#Q2. Make a thread that prints numbers from 1-10, waits for 1 sec between

import thread
import time

class random(thread):
    def run(self):
        for x in range(0,10):
            print x
            time.sleep(1)
def run():
    random().start()


#Q3 .
import thread
import time

list = [1, 2, 3, 4, 5]
def display():
    print list
    time.sleep(2)




