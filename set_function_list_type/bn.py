import struct


def type_defer(bv, type_name):
    return bv.types[type_name].pointer(
        binaryninja.architecture.Architecture["x86_64"], bv.types[type_name]
    )


data = bv.read(0x1C004F3B0, 0x1C004F600 - 0x1C004F3B0)


for i in range(0, len(data), 8):
    address = struct.unpack("<Q", data[i : i + 8])[0]
    function = bv.get_function_at(address)
    if function == None:
        continue

    if len(function.parameter_vars) == 0:
        continue
    print(f"address = {hex(address)}")
    function.parameter_vars[0].type = type_defer(bv, "PFILE_OBJECT")
