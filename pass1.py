import maplist
import re

def pass1(lines):
    symboltable = {}
    length = 0
    for line in lines:
        line=line.upper()
        line = line.lstrip().rstrip()
        if "EXTRN" in line:
            continue;
        if ':' in line:
            if "DB" in line.split(":")[1].lstrip().rstrip():
                symboltable[line.split(":")[0].lstrip().rstrip()]=[length,"v"]
                length+=line.count(",")+1
            elif "DS" in line.split(":")[1].lstrip().rstrip():
                symboltable[line.split(":")[0].lstrip().rstrip()]=[length,"v"]
                length+=int(line.split(":")[1].lstrip().rstrip().split(" ")[1].lstrip().rstrip())
            elif "EQU" in line.split(":")[1].lstrip().rstrip():
                symboltable[line.split(":")[0].lstrip().rstrip()]=[line.split(":")[1].lstrip().rstrip().split(" ")[-1].lstrip().rstrip(),"c"]
            else:
                symboltable[line.split(":")[0].lstrip().rstrip()]=[length,"v"]
                length+= int(maplist.opcode_map[line.split(":")[1].lstrip().rstrip().split(" ")[0].lstrip().rstrip()])
                
        else:
            length+=int(maplist.opcode_map[line.split(" ")[0].lstrip().rstrip()])
    return symboltable, length
    
                
def out(symboltable,lines):
    for i in symboltable:
        for j in range(0,len(lines)):
            lines[j]=lines[j].upper()
            lines[j]=lines[j].lstrip().rstrip()
            if i in lines[j]:
                if(symboltable[i][1]=="c"):
                    s=str(symboltable[i][0])
                else:
                    s="OFFSET "+str(symboltable[i][0])+" "
                lines[j]=lines[j].replace(i,s)
    
    for j in range(0,len(lines)):
        if ":" in lines[j]:
            lines[j]=lines[j].split(":")[1].lstrip().rstrip()
        if "+" in lines[j]:
            t1=int(lines[j].split("+")[0].lstrip().rstrip().split(" ")[-1].lstrip().rstrip())
            t2=int(lines[j].split("+")[1].lstrip().rstrip().split(" ")[0].lstrip().rstrip())
            lines[j]=re.sub(r'(\d)*\s\+(\d)*',str(t1+t2) + " ",lines[j])
        elif "-" in lines[j]:
            t1=int(lines[j].split("-")[0].lstrip().rstrip().split(" ")[-1].lstrip().rstrip())
            t2=int(lines[j].split("-")[1].lstrip().rstrip().split(" ")[0].lstrip().rstrip())
            lines[j]=re.sub(r'(\d)*\s\-(\d)*',str(t1-t2) + " ",lines[j])
    return lines
