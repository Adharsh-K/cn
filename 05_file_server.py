import socketserver
from pathlib import Path

class FileHandler(socketserver.BaseRequestHandler):
    def handle(self):
        filename, sock = self.request
        path = Path(filename.decode()).name  # only allow a file in this folder
        try:
            data = Path(path).read_bytes()
            # Send chunks; this simple demo assumes a small file and a local network.
            for start in range(0, len(data), 1024):
                sock.sendto(data[start:start + 1024], self.client_address)
            sock.sendto(b"__END__", self.client_address)
        except FileNotFoundError:
            sock.sendto(b"__ERROR__", self.client_address)

server = socketserver.ThreadingUDPServer(("127.0.0.1", 5004), FileHandler)
print("UDP file server running. Put files in this folder.")
server.serve_forever()
