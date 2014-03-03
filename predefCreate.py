name= raw_input("Enter the name of your predefined function:\n")
name = name.upper().lstrip().rstrip()

predef_file = file("predef.txt","a")

predef = raw_input("Enter the instructions for the predefined function (separated by a semicolon):\n")
predef = predef.lstrip().rstrip()
lines = predef.split(";")
string = ""

for line in lines:
    string = string + "#" +line

predef_file.write(name + string + '\n')
predef_file.close()
