import maplist
import re
import pass1
import translation
import predefExpand
import macroExpand

print "Enter file name: "
file_name = raw_input()


temp = file(file_name)
code = temp.read()
lines = code.split("\n")
temp.close()

for i in range(len(lines)):
    lines[i] = lines[i].lstrip().rstrip().upper()


print "Enter language of the file: "
language_input = raw_input ()
lines=macroExpand.macroExpand(lines)
lines=predefExpand.predefExpand(lines)

lines = translation.translate(language_input,lines)

for line in lines:
    print line



symboltable, length = pass1.pass1(lines)
lines = pass1.out(symboltable,lines)
print lines
temp1 = file(file_name.split('.')[0]+'1.txt', 'w')
for line in lines:
    temp1.write(line+'\n')
temp1.write('#\n')

for key in symboltable:
    temp1.write(key + "$" + str(symboltable[key][0]) + "$" +str(symboltable[key][1]) + "\n")
temp1.write("#\n" + str(length) + "\n")
    
temp1.close()


