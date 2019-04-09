from multiprocessing import Pool
import os,time

def fun(pim):
    time.sleep(1)
    print('p%d pid %d' % (pim,os.getpid()))

def main():
    pool = Pool(4)
    # while True:
    for i in range(20):
        pool.apply_async(fun,args=(i,))
        # pool.apply(fun,(i,))

    pool.close()
    time.sleep(3)
    pool.terminate()
    # pool.join()
    print('finish')

if __name__ == '__main__':
    main()