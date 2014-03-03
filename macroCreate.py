name= raw_input("Enter the name of your macro:\n")
name = name.upper().lstrip().rstrip()

macro_file = file("macros.txt","a")

macro = raw_input("Enter the instructions for the macro (separated by a semicolon):\n")
macro = macro.lstrip().rstrip()
lines = macro.split(";")
string = ""

for line in lines:
    string = string + "#" +line

macro_file.write(name + string + '\n')
macro_file.close()
