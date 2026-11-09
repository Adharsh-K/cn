import socket

s = socket.socket()
s.bind(("127.0.0.1", 5000))
s.listen(1)
print("Matrix server running...")

conn, addr = s.accept()
rows, cols = map(int, conn.recv(100).decode().split())

if rows == cols:
    result = "Square matrix"
elif rows == 1:
    result = "Row matrix"
elif cols == 1:
    result = "Column matrix"
else:
    result = "Rectangular matrix"

conn.send(result.encode())
conn.close()
s.close()
