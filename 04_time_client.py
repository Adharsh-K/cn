import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(b"TIME", ("127.0.0.1", 5003))
reply, _ = s.recvfrom(1024)
print("Server time:", reply.decode())
s.close()
