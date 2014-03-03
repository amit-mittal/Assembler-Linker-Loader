def translate (language_input,code):    
    language_input = language_input.upper()
    language_file = file(language_input + ".txt")
    language_map = {}
    temp = language_file.read()
    lines = temp.split ("\n")
    language_file.close()
    
    for line in lines:
        if "#" in line:
            language_map[line.split("#")[0].upper().lstrip().rstrip()] = line.split("#")[1].upper().lstrip().rstrip()
    for index in language_map:
        for i in range(len(code)):
            if (index + ' ') in code[i]:
                code[i] = code[i].replace(index,language_map[index])
    return code

