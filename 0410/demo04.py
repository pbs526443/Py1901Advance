# 1. 引入socket模块
from socket import *
import threading
import time

# 2. 构造服务端socket对象
# serversocket = socket(AF_INET,SOCK_DGRAM)
# 3. 绑定地址
# saddr = ('192.168.12.168',50000)
# serversocket.bind(saddr)
# result,addr = serversocket.recvfrom(1024)
# print(addr)
# print(serversocket)
# while True:
#     result = serversocket.recvfrom(1024)
#     print(result)

# input1 = input('请输入值')
# serversocket.sendto(input1.encode('utf-8'),addr)

def read(serversocket):
    while True:
        result = serversocket.recvfrom(1024)
        print(result)

def write(serversocket,addr):
    while True:
        input1 = input('请输入值')
        serversocket.sendto(input1.encode('utf-8'), addr)

def main():
    serversocket = socket(AF_INET, SOCK_DGRAM)
    saddr = ('192.168.12.168', 50000)
    serversocket.bind(saddr)
    result, addr = serversocket.recvfrom(1024)
    print(result.decode('utf8'),addr)
    t1 = threading.Thread(target=read,args=(serversocket,))
    t2 = threading.Thread(target=write,args=(serversocket,addr))
    t1.start()
    t2.start()

if __name__ == '__main__':
    main()