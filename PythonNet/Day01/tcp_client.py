from socket import *

#创建客户端套接字要和服务器类型相同
connfd = socket(AF_INET,SOCK_STREAM)

#地址
HOST = '10.34.10.48'
PORT = 8888
ADDR = (HOST,PORT)
BUFFERSIZE = 1024

#连接请求
connfd.connect(ADDR)
while True:
    #进行通信
    data = input("input: ")
    if not data:
        print("data is null,close",ADDR)
        break
    connfd.send(data.encode())
    print("connect to:",ADDR)
    print("recv",connfd.recv(BUFFERSIZE).decode())


connfd.close()