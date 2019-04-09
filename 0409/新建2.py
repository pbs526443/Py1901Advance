from multiprocessing import Queue,Process
import time

def read(q):
    while True:
        print('pqueue size %d' % q.qsize())
        r = q.get()
        print('get %d ' % r)
        print('pqueue size %d ' % q.qsize())

def write(q):
    for r in range(5):
        q.put(r)
        print('put %d ' % r)
        print('queue size %d ' % q.qsize())
        time.sleep(2)

def main():
    q = Queue(10)
    q.put(-1)
    q.put(-2)

    try:
        # put_nowwait 不会等待队列有空闲位置再放入数据，如果数据放入不成功就直接崩溃
        q.put_nowait(-3)
    except:
        print('put_nowait arror')

    # pr = Process(target=read,args=(q,))
    pw = Process(target=write,args=(q,))
    # pr.start()
    pw.start()

    # pr.join()
    pw.join()

    try:
        # get_nowait 取值时不等待，取不到会直接崩溃
        first = q.get_nowait()
        print(first)
    except:
        print('get_nowait error')

    print('finish')

if __name__ == '__main__':
    main()

'''
Queue(n) 初始化队列
get() 阻塞取，取不出来一直等待
put() 阻塞方法，放不进去就一直等待
get_nowait() 取值不等待，取不到就直接崩溃
put_nowait() 不会等待有空闲位置再放入数据，如果数据放不进去就直接崩溃
'''