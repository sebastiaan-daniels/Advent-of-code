import enum


with open('in8.txt','r') as f:
    instructions = [x.strip() for x in f.readlines()]
    # strip all double backslashes
    

new_instr = []
for line in instructions:
    print(line)
    new_line = ""
    for index in range(0,len(line)-1):
        if line[index+1] != '\\':
            new_line += line[index]
    new_instr.append(new_line)
    print(new_line)
