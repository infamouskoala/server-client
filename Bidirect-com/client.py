import socket
koala = socket.socket()

ip = "127.0.1.1"
port = 8080

koala.connect((ip, port))
while True:
    print(koala.recv(1024).decode())
    x = input("msg: ")
    koala.send(x.encode())