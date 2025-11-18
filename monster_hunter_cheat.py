from pymem import Pymem
from pymem.ptypes import RemotePointer

mem = Pymem('MonsterHunterWorld.exe')
offsets = [0x110, 0x58, 0x18, 0x18, 0x18, 0x10, 0x114]
base_address = mem.base_address + 0x051D0CA8
k = RemotePointer(mem.process_handle, base_address)
for offset in offsets:
    if offset == offsets[-1]:
        k = k.value + offset
        break
    k = RemotePointer(mem.process_handle, k.value + offset)
print(mem.read_int(k))
mem.write_int(k, 99999999)