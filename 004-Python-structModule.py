import struct
import ctypes
'''
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
'''
#pack-unpack

size = struct.calcsize('hh')
buff = ctypes.create_string_buffer(size)

struct.pack_into('hh', buff, 0, 1, 8)

pck = struct.unpack_from('h', buff, 2)
print(pck)

record = b'raymond   \x32\x12\x08\x01\x08'
name, serialnum, school, gradelevel = struct.unpack('>10sHHb', record)

from collections import namedtuple
Student = namedtuple('Student', 'name serialnum school gradelevel')
Student._make(struct.unpack('<10sHHb', record))
print(serialnum)