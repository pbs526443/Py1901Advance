from multiprocessing import Process
import os,time

def p1process():
    while True:
        time.sleep(1)
        print('p1 pid %d parentpid %d' % (os.getpid(), os.getppid()))

def p2process():
    while True:
        time.sleep(1)
        print('p2 pid %d parentpid %d' % (os.getpid(), os.getppid()))

def main():
    print('main pid %d parentpid %d' % (os.getpid(), os.getppid()))
    p1 = Process(target=p1process)
    p2 = Process(target=p2process)
    p1.start()
    p2.start()
    print(p1.name,p1.pid)
    print(p2.name,p2.pid)
    time.sleep(3)
    p1.terminate()
    time.sleep(1)
    print(p1.is_alive())
    print(p2.is_alive())
    p2.join()


if __name__ == '__main__':
    main()