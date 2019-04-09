from multiprocessing import Pool,Manager,Process
import time

def pdo(r):
    print(r+'任务开启')
    return r

def read(q):
    while True:
        r = q.get()
        print('get %d ' % r)
        # p1 = Process(target=pdo,args=(r,))
        # p1.start()
        time.sleep(1)

def write(q):
    for i in range(10):
        q.put(i)



def main():
    q = Manager().Queue(5)
    pool = Pool(10)

    pool.apply_async(write,(q,))
    pool.apply_async(read,(q,))
    pool.close()
    pool.join()
    print('finish')


if __name__ == '__main__':
    main()
