# from socket import *
import threading,socket
import time

# while True:
#     time.sleep(1)
#     clientsocket.sendto("hello".encode("utf8"),addr)

# clientsocket.sendto("hello".encode("utf8"),addr)

def wirte(clientsocket,addr):
    while True:
        time.sleep(1)
        clientsocket.sendto("hello".encode("utf8"),addr)

def read(clientsocket,BUFFER_SIZE):
    time.sleep(1.5)
    while True:
        info, ADDR = clientsocket.recvfrom(BUFFER_SIZE)
        print(info.decode('utf8'), ADDR)

def main():
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    addr = ('127.0.0.1', 60000)
    BUFFER_SIZE = 1024
    t2 = threading.Thread(target=wirte,args=(clientsocket,addr))
    t1 = threading.Thread(target=read,args=(clientsocket,BUFFER_SIZE))
    t1.start()
    t2.start()


if __name__ == '__main__':
    main()