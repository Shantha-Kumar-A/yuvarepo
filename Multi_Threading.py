from time import sleep
from threading import *

class hello(Thread): # become sub class of super class Thread situated in threading module

    def run(self):  #method overriding happened here run method which was available in Thread class, so dont change
        for i in range(5):
            print('Hello')
            sleep(1)

class hi(Thread):  # become sub class of super class Thread situated in threading module

    def run(self):
        for i in range(5):
            print('Hi')
            sleep(1)

t1 = hello()
t2 = hi()

t1.start()
sleep(0.2)
t2.start()

t1.join()  #waiting for the thread t1 to complete their process to go further statements 
t2.join()  #waiting for the thread t2 to complete their process to go further statements
#bye will be executed once both the threads t1 and t2 has been finished execution
print('bye')
