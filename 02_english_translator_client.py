import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
message = input("Enter short-form English: ")
s.sendto(message.encode(), ("127.0.0.1", 5001))
reply, _ = s.recvfrom(1024)
print("Translated:", reply.decode())
s.close()
