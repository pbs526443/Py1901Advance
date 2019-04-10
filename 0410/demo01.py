import threading
import time

def threading1():
    if lock1.acquire() :
        print('1')

def threading2():
    if lock2.acquire():
        print('2')
        lock3.release()

def threading3():
    if lock3.acquire():
        print('3')
        lock1.release()

if __name__ == '__main__':

    lock1 = threading.Lock()
    lock1.acquire()
    lock2 = threading.Lock()
    lock3 = threading.Lock()
    lock3.acquire()

    t1 = threading.Thread(target=threading1)
    t2 = threading.Thread(target=threading2)
    t3 = threading.Thread(target=threading3)

    t1.start()
    t2.start()
    t3.start()