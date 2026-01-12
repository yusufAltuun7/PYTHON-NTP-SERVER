import socket
from _socket import SOCK_DGRAM
from idlelib.iomenu import encoding

sock = socket.socket(socket.AF_INET, socket. SOCK_DGRAM)
sock.bind(('127.0.0.105', 12456))


while True:
    print('deneme')
    data1, addr1 = sock.recvfrom(4096)
    data2, addr2 = sock.recvfrom(4096)
    print(str(data1))
    print(str(data2))
    sock.sendto(str("120126").encode('ascii'),addr1)
    sock.sendto(str(data2).encode('ascii'),addr2)