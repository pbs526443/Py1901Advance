from multiprocessing import Process
import time,threading

class MyProcess(Process):
    def run(self):
        while True:
            print('hi')
            time.sleep(1)

# 进程封装类
class Mythread(threading.Thread):
    def run(self):
        while True:
            print('h1')
            time.sleep(1)

# 线程封装类
def thmain():
    t = Mythread()
    t.start()


def main():
    p = MyProcess()
    p.start()

if __name__ == '__main__':
    # main()
    thmain()