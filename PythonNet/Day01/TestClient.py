from socket import *
host = '192.168.88.108'
port = 9999
addr = (host,port)
conn = socket()
conn.connect(addr)
while True:
    data = input("发送->>")
    if not data:
        break
    conn.send(data.encode())
    data = conn.recv(1024)
    print('从服务端接收:',data.decode())

conn.close()