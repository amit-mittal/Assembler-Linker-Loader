def predefExpand (code):    
    predef_file = file("predef.txt")
    predef_map = {}
    temp = predef_file.read()
    lines = temp.split ("\n")
    predef_file.close()
    output = []
    j=0
    for line in lines:
        if "#" in line:
            list = []
            for i in range(len(line.split("#"))-1):
                list.append(line.split("#")[i+1].lstrip().rstrip())
            predef_map[line.split("#")[0].upper().lstrip().rstrip()] = list

     
    for i in range(len(code)):
        if 'ADDRR' in code[i]:
                if ':' in code[i]:
                    arg1=code[i].split(':')[1].lstrip().rstrip().split(' ')[1].split(',')[0].lstrip().rstrip()
                    arg2=code[i].split(':')[1].lstrip().rstrip().split(' ')[1].split(',')[1].lstrip().rstrip()
                    output.append(code[i].split(':')[0].lstrip().rstrip()+': MOV A,'+arg1)
                    output.append("ADD "+arg2)
                    output.append("MOV "+arg1+",A")
                else:
                    arg1=code[i].lstrip().rstrip().split(' ')[1].split(',')[0].lstrip().rstrip()
                    arg2=code[i].lstrip().rstrip().split(' ')[1].split(',')[1].lstrip().rstrip()
                    output.append("MOV A,"+arg1)
                    output.append("ADD "+arg2)
                    output.append("MOV "+arg1+",A")
        elif 'SUBRR' in code[i]:
            if ':' in code[i]:
                    arg1=code[i].split(':')[1].lstrip().rstrip().split(' ')[1].split(',')[0].lstrip().rstrip()
                    arg2=code[i].split(':')[1].lstrip().rstrip().split(' ')[1].split(',')[1].lstrip().rstrip()
                    output.append(code[i].split(':')[0].lstrip().rstrip()+': MOV A,'+arg1)
                    output.append("SUB "+arg2)
                    output.append("MOV "+arg1+",A")
            else:
                    arg1=code[i].lstrip().rstrip().split(' ')[1].split(',')[0].lstrip().rstrip()
                    arg2=code[i].lstrip().rstrip().split(' ')[1].split(',')[1].lstrip().rstrip()
                    output.append("MOV A,"+arg1)
                    output.append("SUB "+arg2)
                    output.append("MOV "+arg1+",A")
        else:            
            if ":" in code[i]:
                keyword = code[i].lstrip().rstrip().split(":")[1].lstrip().rstrip().split(" ")[0].lstrip().rstrip()
            else:
                keyword = code[i].lstrip().rstrip().split(" ")[0]
            keyword = keyword.lstrip().rstrip()

            if keyword in predef_map:
                counter = 0
                counter = len(predef_map[keyword])
            
                
                if ':' in code[i]:
                    if "FACTORIAL" in keyword:
                        argument = code[i].split(':')[1].lstrip().rstrip().split(" ")[1].lstrip().rstrip()
                        output.append("VARIABILITY: EQU "+argument)
                    output.append(code[i].split(':')[0].lstrip().rstrip()+': '+predef_map[keyword][0])
                else:
                    if "FACTORIAL" in keyword:
                        argument = code[i].lstrip().rstrip().split(" ")[1].lstrip().rstrip()
                        print argument
                        output.append("VARIABILITY: EQU "+argument)
                    output.append(predef_map[keyword][0])
                for k in range(1, counter):
                    output.append(predef_map[keyword][k])
                    j+=1
            else:
                output.append(code[i])
                j+=1
                    
    return output


