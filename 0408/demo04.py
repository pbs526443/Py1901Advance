from multiprocessing import Process
import os

def plprocess():
    print('p1 pid %d' % os.getpid(),os.getppid())
    print('进程p1执行了')

class MyProcess(Process):
    def __init__(self):
        Process.__init__(self)
    def run(self):
        print('run执行了',os.getpid())

def main():
    p1 = MyProcess()
    p1.start()
    p1.join()
    print('finish',os.getpid(),os.getppid())

if __name__ == '__main__':
    main()