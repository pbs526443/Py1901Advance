import os,time
from multiprocessing import Process

# p1 进程入口函数
def plprocess():
    while True:
        time.sleep(1)
        print('p1 pid %d' % os.getpid())
        print('进程p1执行了')
def p2process():
    while True:
        time.sleep(1)
        print('p2 pid %d' % os.getpid())
        print('进程p2执行了')

def main():
    # 1. 创建进程，创建Process类的实例
    # 2. 通过Process指定进程入口函数
    p1 = Process(target=plprocess)
    p2 = Process(target=p2process)
    # 3. 开启进程
    p1.start()
    # p1.join()
    p2.start()
    # p2.join()
    print(p1.is_alive())
    print(p2.is_alive())
    time.sleep(3)
    p1.terminate()
    time.sleep(1)
    print(p1.is_alive())
    print(p2.is_alive())


if __name__ == '__main__':
    print('main pid %d pycharm pid %d' % (os.getpid(),os.getppid()))
    main()