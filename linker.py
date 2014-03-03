import pass1
import re

base_address = 0

print "Enter number of programs: "
num_prog = int(raw_input())

code = {}
symboltable = {}
length = {}
base_address = {}

for i in range(num_prog):
    print "Enter the file name: "
    prog_name = raw_input()

    print "Base address: "
    base = int(raw_input())
    base_address[i+1] = base

    temp = file(prog_name)
    code_temp = temp.read()

    lines_temp = code_temp.split('#')[0].lstrip().rstrip()
    lines= lines_temp.split("\n")
    code[i+1]=lines
    
    symboltable_temp = code_temp.split('#')[1].lstrip().rstrip()
    symboltable_lines=symboltable_temp.split('\n')
    dict_temp = {}
    for line in symboltable_lines:
        dict_temp[line.split('$')[0].lstrip().rstrip()] = [line.split('$')[1].lstrip().rstrip(),line.split('$')[2].lstrip().rstrip()]
    symboltable[i+1] = dict_temp

    length[i+1] = int(code_temp.split('#')[2].lstrip().rstrip())


for i in range(num_prog):
    arr=[]
    lines=code[i+1]
    for j in range(0,len(lines)):
        if "EXTRN" in lines[j]:
            temp= lines[j].split(" ")[-1].lstrip().rstrip()
            arr=temp.split(",")
            lines[j]=";"+lines[j]
        if "OFFSET" in lines[j]:
            t1=int(lines[j].split("OFFSET")[1].lstrip().rstrip().split(" ")[0].lstrip().rstrip())
            lines[j]=re.sub("OFFSET"+r'(\s)(\d)*',str(base_address[i+1]+t1),lines[j])
    if len(arr)>0:

        temp=" "
        for z in arr:
            for index in range(num_prog):
                if z in symboltable[index+1]:
                    if symboltable[index+1][z][1]=="v":
                        temp=str(int(symboltable[index+1][z][0])+base_address[i+1])
                        #print str(int(symboltable[index+1][z][0])+base_address[i+1])
                        break
                    else:
                        temp=symboltable[index+1][z][0]
                        #print symboltable[index+1][z][0]
                        break
            for index in range(len(lines)):
                lines=code[i+1]
                if z in lines[index]:
                    if ";" in lines[index]:
                        continue;
                    lines[index]=lines[index].replace(z,temp)
for i in range(num_prog):
    lines=code[i+1]
    for j in range(0,len(lines)):
        print lines[j]

temp1=file("l1.txt",'w')
for i in range(num_prog):
    lines=code[i+1]
    for j in range(0,len(lines)):
        if "HLT" in lines[j] and i!=num_prog-1:
            continue;
        temp1.write(lines[j]+'\n')
    
        
        
    
                    
            
        
        
            
            
    
