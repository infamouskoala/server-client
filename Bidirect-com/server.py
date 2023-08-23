import socket

s = socket.socket()
s.bind(("127.0.1.1", 8080))
print("SERVER IS READY")

s.listen(5)
c, addr = s.accept()
c.send("Welcome.".encode())

while True:
    print(c.recv(1024).decode())
    x = input("msg: ")
    c.send(x.encode())