'''
#NTP Zaman Etiketlerini görme amaçlı yazıldı.

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

#Zaman etiketlerini pack etme

import struct
import ctypes
import time

NTP_DELTA = 2208988800 #70 yıl(unix - ntp arası fark)

current_time = time.time() + NTP_DELTA
print(current_time)
sec = int(current_time)
print(sec)
frac = int((current_time - sec)*(2**32))
print(frac)

timeStamp = struct.pack('!II', sec, frac)
print(timeStamp)

'''
#ntp server'ına response atıp cevabını aldığımız yazılım

import socket
import struct
import time

NTP_DELTA = 2208988800                                      #70 yıl değişkeni
host = "time.windows.com"
port = 123

                                                            # 48 byte boş paket (ilk byte: LI/VN/Mode = 0b00 100 011  = 0x23)
msg = b'\x23' + 47 * b'\0'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)     #AF_INET = IPv4    SOCK_DGRAM = UDP PORT
sock.settimeout(3)
sock.sendto(msg, (host, port))

data, _ = sock.recvfrom(1024)
print(time.time())
print(data)
print('\n\n',struct.unpack("!12I", data),'\n\n')            # ! || > big endian    #I = 4 Byte    #!12I = big endian 48 byte veri paketi
if data:
    unpacked = struct.unpack("!12I", data)
    transmit_timestamp = unpacked[10] + float(unpacked[11]) / 2**32
    print(unpacked[10])                                     # 8 byte NTP'den gelen zaman verisi 10 ve 11 son iki 4 byte yani 8 byte'lık veri
    print(float(unpacked[11]) / 2**32)                      # ilk 4 byte genel son 4 byte ise daha hassas saat ayarı için
    unix_time = transmit_timestamp - NTP_DELTA              # alınan zamandan 70 yıl sabitini çıkarınca unix tabanlı bir saniye değeri geliyor
    print("NTP Zamanı:", time.ctime(unix_time))             #bu saniye değeri de time fonksiyonunda yerine koyarsak anlık değeri net buluyoruz