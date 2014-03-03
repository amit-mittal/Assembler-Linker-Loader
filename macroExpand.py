def macroExpand (code):    
    macro_file = file("macros.txt")
    macro_map = {}
    temp = macro_file.read()
    lines = temp.split ("\n")
    macro_file.close()
    output = []
    j=0
    for line in lines:
        if "#" in line:
            list = []
            for i in range(len(line.split("#"))-1):
                list.append(line.split("#")[i+1].lstrip().rstrip())
            macro_map[line.split("#")[0].upper().lstrip().rstrip()] = list


    for i in range(len(code)):
        if ":" in code[i]:
            keyword = code[i].lstrip().rstrip().split(":")[1].lstrip().rstrip().split(" ")[0].lstrip().rstrip()
        else:
            keyword = code[i].lstrip().rstrip().split(" ")[0]
        keyword = keyword.lstrip().rstrip()

        if keyword in macro_map:
            counter = 0
            counter = len(macro_map[keyword])

            if ':' in code[i]:
                output.append(code[i].split(':')[0].lstrip().rstrip()+': '+macro_map[keyword][0])
            else:
                output.append(macro_map[keyword][0])
            for k in range(1, counter):
                output.append(macro_map[keyword][k])
                j+=1
        else:
            output.append(code[i])
            j+=1
                
    return output
