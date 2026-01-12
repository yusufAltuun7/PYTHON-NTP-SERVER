#burası merkezi bir notepad!!
'''
    1)UDP server

import socket
from _socket import SOCK_DGRAM
from idlelib.iomenu import encoding

sock = socket.socket(socket.AF_INET, socket. SOCK_DGRAM)
sock.bind(('127.0.0.10', 12456))


while True:
    print('deneme')
    data1, addr1 = sock.recvfrom(4096)
    data2, addr2 = sock.recvfrom(4096)
    print(str(data1))
    print(str(data2))
    sock.sendto(str(data1).encode('ascii'),addr1)
    sock.sendto(str(data2).encode('ascii'),addr2)
    
    UDP Server kurulumu -- test edildi ve şu an UDP port üzerinden istenildiği gibi echoing yapılabilmekte
    
############################################################################################################################################################################################################################################

from test.test_buffer import struct_items, struct
from _struct import Struct
from test.test_ctypes.test_generated_structs import struct_or_union
from test.test_zipimport import NOW

    2)UDP client

import socket
from _socket import SOCK_DGRAM
from idlelib.iomenu import encoding
from _overlapped import NULL
client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
msg1 = 'dere boyu kavaklar'
msg2 = 'acti yesil yapraklar'
client_sock.sendto(msg1.encode(encoding="utf-8", errors="ignore"),('127.0.0.10', 12456))
client_sock.sendto(msg2.encode(encoding="utf-8", errors="ignore"),('127.0.0.10', 12456))
#print("kontrol 1")
data1, addr1 = client_sock.recvfrom(4096)
data2, addr2 = client_sock.recvfrom(4096)
print("serverdan bana gelen cevap:")
print(str(data1))
print(str(data2))
#print(str(data))
client_sock.close()

    UDP Client Kurulumu -- test edildi ve şu an UDP port üzerinden istenildiği gibi echoing yapılabilmekte

####################################################################################################################

   3)python struct

from struct import *
import ctypes

# pack values into binary

for x in range (12,15):
    if(x%2 == 0):
        var = struct.pack('l',x)
        print("\n")
        print(var)
        
    else:
        var = struct.pack('i',x)
        print("\n")
        print(var)

unp = struct.unpack('i', var)
print(unp)

print(struct.calcsize('hhlq?'))

pack-unpack

size = struct.calcsize('hh')
buff = ctypes.create_string_buffer(size)

struct.pack_into('hh', buff, 0, 1, 8)

pck = struct.unpack_from('h', buff, 2)
print(pck)

record = b'raymond   \x32\x12\x08\x01\x08'
name, serialnum, school, gradelevel = unpack('>10sHHb', record)

from collections import namedtuple
Student = namedtuple('Student', 'name serialnum school gradelevel')
Student._make(unpack('<10sHHb', record))
print(serialnum)

########################################################################3

Time fonksiyonu kullanıldı
import time

def now():
    return time.time()

# T1 = Clien'ın Servere İstek Attığı An
# T2 = Server'ın Client'ten İstek Aldığı An
# T3 = Server'ın Client'a Cevabı Verdiği An
# T4 = Client'ın Server'ın Cevabını Aldığı An

T1 = now()
time.sleep(0.2)
print('T1:', T1)

T2 = now()
time.sleep(0.2)
print('T2:', T2)

T3 = now()
time.sleep(0.2)
print('T3:', T3)

T4 = now()
time.sleep(0.2)
print('T4:', T4)

delay = (T4-T1)-(T3-T2)
print('Delay:',delay)

offset = (T2-T1)-(T3-T4)/2
print('Offset:',offset)

A = now()
print(time.ctime(A))

####################################################################################################################

# binary paket oluşturma
import struct as st
import ctypes
import time

NTP_DELTA = 2208988800

current_time = time.time() + NTP_DELTA
print(current_time)
sec = int(current_time)
print(sec)
frac = int((current_time - sec)*(2**32))
print(frac)

timeStamp = struct.pack('!II', sec, frac)
print(timeStamp)

####################################################################################################################

import socket
import struct
import time

NTP_DELTA = 2208988800
host = "time.windows.com"
port = 123

# 48 byte boş paket (ilk byte: LI/VN/Mode = 0b00 100 011  = 0x23)
msg = b'\x23' + 47 * b'\0'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(3)
sock.sendto(msg, (host, port))

data, _ = sock.recvfrom(1024)
print(time.time())
print(data)
print('\n\n',struct.unpack("!12I", data),'\n\n')
if data:
    unpacked = struct.unpack("!12I", data)
    transmit_timestamp = unpacked[10] + float(unpacked[11]) / 2**32
    print(unpacked[10])
    print(float(unpacked[11]) / 2**32)
    unix_time = transmit_timestamp - NTP_DELTA
    print("NTP Zamanı:", time.ctime(unix_time))
    

####################################################################################################################
'''

import socket
import struct
import time

NTP_DELTA = 2208988800

def system_to_ntp_time(timestamp):
    seconds = int(timestamp) + NTP_DELTA
    fraction = int((timestamp - int(timestamp)) * (2**32))
    return seconds, fraction

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("127.168.1.0", 123))

print("NTP Server çalışıyor...")

while True:
    data, addr = sock.recvfrom(1024)
    print("1")
    # 48 byte değilse NTP paketi değildir
    if len(data) < 48:
        continue

    # İstemcinin Transmit Timestamp'i (T1)
    unpacked = struct.unpack("!12I", data)
    orig_ts_sec = unpacked[10]
    orig_ts_frac = unpacked[11]

    # Şu anki zaman (server'nın T3'ü)
    now = time.time()
    tx_sec, tx_frac = system_to_ntp_time(now)

    # Cevap paketi
    response = b'\x1c' + 47 * b'\0'  # 0x1C → LI=0, VN=4, Mode=4 (server)

    # Pakete timestamp yazalım (son 64 bit)
    response = response[:40] + struct.pack("!II", tx_sec, tx_frac)

    sock.sendto(response, addr)

    print(f"Gönderildi → {addr[0]}:{addr[1]}")
