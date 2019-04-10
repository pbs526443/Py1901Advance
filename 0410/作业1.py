import socket

# socket 套接字常用操作
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# bind()绑定端口到一个套接字上
s.bind('192.168.12.168',60000)
# listen()设置并启动TCP监听
s.listen()
# accept()等待客户端连接
s.accept()
# connect()连接指定服务器
s.connect('192.168.12.168')
# recv0接收TCP消息
s.recv()
# send()发送TCP消息
s.send()
# recvfrom()接收UDP消息
s.recvfrom()
# sendto()发送UDP消息
s.sendto()
# close()关闭套接字对象
s.close()


