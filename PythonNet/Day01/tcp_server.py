#python网络套接字模块
#import socket
from socket import *

HOST = '10.34.10.48'
PORT = 8888
ADDR = (HOST,PORT)
BUFFERSIZE = 1024

#创建一个TCP流套接字
sockfd = socket(AF_INET,SOCK_STREAM)
#设置套接字地址
sockfd.bind(ADDR)
#建立套接字监听
sockfd.listen(5)

print("wait for connect.....")

while True:
    #等待客户端请求
    conn,addr = sockfd.accept()
    print("connect from ",addr)
    while True:
        #消息的收发
        data = conn.recv(BUFFERSIZE)
        if not data:
            print("data is null,close conn",addr)
            break
        print("recv:" + data.decode())
        conn.send(b"Recv your message")
        # n = conn.send(b"Recv your message")
        # print("send total %d bytes data:"%n)
        
    #关闭连接    
    conn.close()
#关闭套接字
sockfd.close()
