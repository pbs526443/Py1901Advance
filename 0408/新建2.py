from multiprocessing import Process
import os

def p1process():
    print('p1 pid %d parentpid %d' %(os.getpid(),os.getppid()))

def p2process():
    print('p2 pid %d parentpid %d' % (os.getpid(), os.getppid()))

def main():
    p1 = Process(target=p1process)
    p2 = Process(target=p2process)
    p1.start()
    p2.start()
    print('main process pid %d parentpid %d' %(os.getpid(),os.getppid()))

if __name__ == '__main__':
    main()