import socket
from _socket import SOCK_DGRAM
from idlelib.iomenu import encoding
from _overlapped import NULL

msg = b'\x23' + 47 * b'\0'
client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#msg1 = 'dere boyu kavaklar'
#msg2 = 'acti yesil yapraklar'

client_sock.sendto(msg, ("127.168.1.0", 123))

data1, addr1 = client_sock.recvfrom(4096)
print("serverdan bana gelen cevap:")
print(str(data1))
'''
#client_sock.sendto(msg2.encode(encoding="utf-8", errors="ignore"),('127.0.0.10', 12456))
#print("kontrol 1")


data1, addr1 = client_sock.recvfrom(4096)
data2, addr2 = client_sock.recvfrom(4096)
print("serverdan bana gelen cevap:")
print(str(data1))
print(str(data2))
#print(str(data))
'''
client_sock.close()