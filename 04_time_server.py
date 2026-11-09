import socketserver
from datetime import datetime

class TimeHandler(socketserver.BaseRequestHandler):
    def handle(self):
        message, sock = self.request
        reply = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sock.sendto(reply.encode(), self.client_address)

server = socketserver.ThreadingUDPServer(("127.0.0.1", 5003), TimeHandler)
print("Concurrent UDP time server running...")
server.serve_forever()
