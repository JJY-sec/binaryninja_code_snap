import binaryninja
def read_memory_4bytes(bv,start_address, end_address):
    
    current_address = start_address
    i=0
    while current_address <= end_address:
        i+=1
        value = bv.read(current_address, 4)
        little_endian_value = struct.unpack("<I", value)[0]
        print(hex(current_address), i ,hex(little_endian_value))
        current_address += 4

read_memory_4bytes(bv,0x00000001C0050A80, 0x00000001C0050Ba4)