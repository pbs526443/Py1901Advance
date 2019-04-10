from socket import *
import threading,time

def read(sc):
    while True:
        result = sc.recvfrom(1024)
        print(result)

def wirte(sc,addr):
    while True:
        result = input('请输入你的消息')
        sc.sendto(result.encode('utf-8'), addr)

def main():
    sc = socket(AF_INET,SOCK_DGRAM)
    ADDR = ('192.168.12.168',50001)
    sc.bind(ADDR)
    info,addr = sc.recvfrom(1024)
    print(info)
    t1 = threading.Thread(target=read,args=(sc,))
    t2 = threading.Thread(target=wirte,args=(sc,addr))
    t1.start()
    t2.start()
    t1.join()
    t2.join()


if __name__ == '__main__':
    main()