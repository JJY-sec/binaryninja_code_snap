fd = open("blocks.txt","w")
for func in bv.functions:
    
    if "mozilla::gfx::" in func.name:
        #fd.write(f"{hex(func.start)}\n")
        for block in func.basic_blocks:
            fd.write(f"{hex(block.start)}\n")
    
    #for block in func.basic_blocks:
    #    fd.write(f"{hex(block.start)}\n")
fd.close()
print("eoe")