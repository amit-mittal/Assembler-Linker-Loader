opcode_len = file("memoryUnsorted.txt")
temp = opcode_len.read()
opcode_list = temp.split("\n")
opcode_map = {}
for entry in opcode_list:
    temp_list = entry.split("#")
    opcode_map[temp_list[0].lstrip().rstrip()] = temp_list[1].lstrip().rstrip()
#print opcode_map
