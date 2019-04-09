from multiprocessing import Process,Queue
import os,time

def read(q):
    while True:
        print('pqueue size %d ' % q.qsize())
        r = q.get()
        print('get %d' % r)
        print('pqueue size %d' % q.qsize())

def wite(q):
    for r in range(5):
        q.put(r)
        print('put %d' % r)
        print('queue size %d ' % q.qsize())
        time.sleep(2)

if __name__ == '__main__':
    q = Queue(10)
    pw = Process(target=wite,args=(q,))
    pw.start()
    pr = Process(target=read, args=(q,))
    pr.start()

    pw.join()
    pr.join()

    print('finish')