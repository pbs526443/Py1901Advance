from socket import *
import time
import threading

def read(sc,BUFFER_SIZE):
    time.sleep(1.5)
    while True:
        rs = sc.recvfrom(BUFFER_SIZE)
        print(rs)

def wirte(sc,ADDR):
    sc.sendto(' '.encode('utf-8'),ADDR)
    while True:
        result = input('请输入你的消息')
        sc.sendto(result.encode('utf-8'),ADDR)



def main():
    sc = socket(AF_INET,SOCK_DGRAM)
    ADDR = ('192.168.12.168',60000)
    BUFFER_SIZE = 1024
    t2 = threading.Thread(target=wirte, args=(sc, ADDR))
    t1 = threading.Thread(target=read,args=(sc,BUFFER_SIZE))
    t1.start()
    t2.start()
    t1.join()
    t2.join()


if __name__ == '__main__':
    main()