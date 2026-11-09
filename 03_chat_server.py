import socket
import threading

clients = []

def handle_client(conn):
    while True:
        try:
            message = conn.recv(1024)
            if not message:
                break
            for client in clients:
                if client != conn:
                    client.send(message)
        except:
            break
    if conn in clients:
        clients.remove(conn)
    conn.close()

server = socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(("127.0.0.1", 5002))
server.listen()
print("Chat server running...")

while True:
    conn, addr = server.accept()
    clients.append(conn)
    threading.Thread(target=handle_client, args=(conn,), daemon=True).start()
