import threading,time

def prt():
    print('++')
    time.sleep(1)

def timecount(f):
    def fun():
        start = time.time()
        f()
        end = time.time()
        print(f.__name__,'消耗',end - start)
    return fun

@timecount
def main():
    for i in range(5):
        prt()

@timecount
def threamain():
    for i in range(5):
        t1 = threading.Thread(target=prt,name='Mythread %d' % i)
        t1.start()
        # print(threading.enumerate())
        print(threading.currentThread())
    t1.join()

if __name__ == '__main__':
    # main()
    threamain()