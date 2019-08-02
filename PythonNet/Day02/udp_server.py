#udp_server

from socket import *

#创建数据报套接字
sockfd = socket(AF_INET,SOCK_DGRAM)

#地址
HOST = '10.34.10.48'
PORT = 8888
ADDR = (HOST,PORT)
BUFFERSIZE = 1024

#绑定本地端口
sockfd.bind(ADDR)