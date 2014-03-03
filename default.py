instruction_set=file("memoryUnsorted.txt")
temp = instruction_set.read()
instruction_set.close()
instruction = temp.split("\n")

make_file = file("DEFAULT.txt","w")

for entry in instruction:  
    make_file.write(entry.split("#")[0].lstrip().rstrip()+" # "+entry.split("#")[0].lstrip().rstrip()+"\n")

make_file.close()
