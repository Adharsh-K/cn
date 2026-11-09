import socket

server = ("127.0.0.1", 5004)
filename = input("Enter filename to download: ")

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.settimeout(2)
s.sendto(filename.encode(), server)

data = bytearray()
try:
    while True:
        chunk, _ = s.recvfrom(2048)
        if chunk == b"__END__":
            with open("downloaded_" + filename.split("/")[-1], "wb") as f:
                f.write(data)
            print("File downloaded.")
            break
        if chunk == b"__ERROR__":
            print("File not found.")
            break
        data.extend(chunk)
except socket.timeout:
    print("Transfer timed out. UDP may lose packets; this is a basic lab demo.")
s.close()
