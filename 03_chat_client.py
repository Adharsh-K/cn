import socket
import threading

s = socket.socket()
s.connect(("127.0.0.1", 5002))

def receive():
    while True:
        try:
            print("\n" + s.recv(1024).decode())
        except:
            break

threading.Thread(target=receive, daemon=True).start()

print("Type messages. Enter 'quit' to exit.")
while True:
    message = input()
    if message.lower() == "quit":
        break
    s.send(message.encode())

s.close()
