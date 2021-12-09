#converter from data to list
with open('inday03-1.txt','r') as f:
    data = [k.rstrip('\n') for k in f.readlines()]


def convert_binary(bin):
    return int(bin,2)

def convert_list_ox(index:int, binary: list) -> list:
    newlist = []
    avg_1 = 0
    avg_0 = 0
    for bin in binary:
        if bin[index] == '0': avg_0 += 1
        else: avg_1 += 1
    if avg_1 >= avg_0: to_find = '1'
    else: to_find = '0'

    for bin in binary:
        if bin[index] == to_find: newlist.append(bin)
    return newlist

def convert_list_co2(index:int, binary: list) -> list:
    newlist = []
    avg_1 = 0
    avg_0 = 0
    for bin in binary:
        if bin[index] == '0': avg_0 += 1
        else: avg_1 += 1
    if avg_1 < avg_0: to_find = '1'
    else: to_find = '0'

    for bin in binary:
        if bin[index] == to_find: newlist.append(bin)
    
    return newlist

#main loop
#oxygen
new_data = data
for index in range(9999999999):
    if len(new_data) == 1: break
    new_data = convert_list_ox(index,new_data)
oxygen = new_data[0]

new_data = data
for index in range(9999999999):
    if len(new_data) == 1: break
    new_data = convert_list_co2(index,new_data)

co2 = new_data[0]
print(oxygen,co2)
oxygen = convert_binary(oxygen)
co2 = convert_binary(co2)
print(oxygen,co2)
print(oxygen* co2)