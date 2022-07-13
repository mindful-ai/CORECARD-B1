import threading
import time
sem = threading.Semaphore()

def fun1():
    while True:
        sem.acquire()
        print(1)
        sem.release()
        time.sleep(0.5)

def fun2():
    while True:
        sem.acquire()
        print(2)
        sem.release()
        time.sleep(0.5)

t = threading.Thread(target = fun1)
t2 = threading.Thread(target = fun2)

t.start()
t2.start()
