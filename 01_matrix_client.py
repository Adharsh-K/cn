import socket

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

s = socket.socket()
s.connect(("127.0.0.1", 5000))
s.send(f"{rows} {cols}".encode())
print("Matrix type:", s.recv(100).decode())
s.close()
