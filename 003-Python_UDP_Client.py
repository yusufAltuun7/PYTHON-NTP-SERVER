import socket
from _socket import SOCK_DGRAM
from idlelib.iomenu import encoding
from _overlapped import NULL

#AF_INET = IPv4
#SOCK_DGRAM = UDP

client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
msg1 = 'Message One: Sending through Client to Server'
msg2 = 'Message Two: Sender is Yusuf ALTUN'
client_sock.sendto(msg1.encode(encoding="utf-8", errors="ignore"),('127.0.0.105', 12456))
client_sock.sendto(msg2.encode(encoding="utf-8", errors="ignore"),('127.0.0.105', 12456))


data1, addr1 = client_sock.recvfrom(4096)
data2, addr2 = client_sock.recvfrom(4096)
print("Incoming messages from Server:")
print(str(data1))
print(str(data2))
#print(str(data))
client_sock.close()