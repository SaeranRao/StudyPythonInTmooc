import sys
import os
from socket import *

HOST = '192.168.88.108'
POST = 9999
ADDR = (HOST,POST)
s = socket()

s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

# s = socket(AF_INET,SOCK_STREAM)
s.bind(ADDR)
s.listen(5)
print('等待消息')
c,addr = s.accept()
while True:
    
    
    print('连接来自:',addr)
    data = c.recv(1024)
    if not data:
        break
    print('收到消息',data.decode())
    c.send(b'recive ur message')
c.close() 
s.close()