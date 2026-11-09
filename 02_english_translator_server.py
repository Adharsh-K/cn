import socket

words = {
    "u": "you",
    "r": "are",
    "ur": "your",
    " gr8": " great",
    "pls": "please",
    "thx": "thanks",
    "b4": "before",
    "2day": "today"
}

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("127.0.0.1", 5001))
print("UDP translator running...")

while True:
    message, addr = s.recvfrom(1024)
    text = message.decode()
    result = " ".join(words.get(word.lower(), word) for word in text.split())
    s.sendto(result.encode(), addr)
