instruction_set=file("instructionSet.txt")
temp = instruction_set.read()
instruction_set.close()
instruction = temp.split("\n")
#language_map = {}
print "Enter the name of your language:"
name= raw_input()
name = name.upper()
make_file = file(name+".txt","w")


for entry in instruction:
    print "Replace " + entry + " with?"
    replacement = raw_input()
    #language_map[entry] = replacement.upper().lstrip().rstrip()
    make_file.write(replacement.upper().lstrip().rstrip()+" # "+entry+"\n")

make_file.close()
