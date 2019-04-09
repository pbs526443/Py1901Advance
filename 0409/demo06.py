import threading,time

def thread1():
    # 子进程 修改主进程变量
    for i in range(1000000):
        lock.acquire()
        global num
        num += 1
        lock.release()

if __name__ == '__main__':
    lock = threading.Lock()

    num = 0
    t1 = threading.Thread(target=thread1)
    t1.start()

    t2 = threading.Thread(target=thread1)
    t2.start()

    # t1.join()
    t2.join()
    # time.sleep(3)
    print(num)