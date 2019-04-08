from multiprocessing import Process
import os

class MyProcess(Process):
    def __init__(self):
        Process.__init__(self)
    def run(self):
        print('Mypid %d parentpid %d' % (os.getpid(),os.getppid()))

def main():
    print('main pid %d parentpid %d' % (os.getpid(),os.getppid()))
    p1 = MyProcess()
    p1.start()

if __name__ == '__main__':
    main()