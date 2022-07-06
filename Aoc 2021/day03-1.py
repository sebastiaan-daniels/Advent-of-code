#importing counters to count most occuring
from collections import Counter

#converter from data to list
with open('inday03-1.txt','r') as f:
    data = [k.rstrip('\n') for k in f.readlines()]

def convert_binary(bin):
    return int(bin,2)

#take the input as a 2d array, with rows and columns.. we will now swap the rows to columns and vice versa
data2 = []
for row in range(len(data[0])):
    row_list = ''
    for column in data:
        row_list += column[row]
    data2.append(row_list)

#calculate gamma
gamma = ''
for item in data2:
    res = Counter(item)
    res = max(res, key = res.get)
    gamma += res

#calculate epsilon by flipping gamma
epsilon = ''
for item in gamma:
    if item == '0': epsilon += '1'
    else: epsilon += '0'

con_gamma = convert_binary(gamma)
con_epsilon = convert_binary(epsilon)
print(con_gamma * con_epsilon)