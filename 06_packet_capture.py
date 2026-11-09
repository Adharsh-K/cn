import socket

# Linux only; run with sudo/root privileges.
# Captures Ethernet frames and displays basic IPv4 protocol information.

s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
print("Capturing packets... Press Ctrl+C to stop.")

try:
    while True:
        packet, addr = s.recvfrom(65535)
        if len(packet) < 34:
            continue

        eth_type = int.from_bytes(packet[12:14], "big")
        if eth_type != 0x0800:  # IPv4 only
            continue

        ip_header = packet[14:34]
        version_ihl = ip_header[0]
        ihl = (version_ihl & 15) * 4
        protocol = ip_header[9]
        source = ".".join(map(str, ip_header[12:16]))
        destination = ".".join(map(str, ip_header[16:20]))

        names = {1: "ICMP", 6: "TCP", 17: "UDP"}
        print(f"{source} -> {destination} | {names.get(protocol, protocol)}")
except KeyboardInterrupt:
    print("\nCapture stopped.")
finally:
    s.close()
