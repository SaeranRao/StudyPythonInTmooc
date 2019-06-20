#python网络套接字模块
#import socket
from socket import *

HOST = '127.0.0.1'
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
#等待客户端请求
conn,addr = sockfd.accept()
print("connect from ",addr)
#消息的收发
data = conn.recv(BUFFERSIZE)
print("接收消息：" + data.decode())
n = conn.send(b"Recv your message")

print("发送%d字节的数据:"%n)

#关闭套接字
# conn.close()
# sockfd.close()
