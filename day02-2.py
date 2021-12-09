#converter from data to list
with open('inday02-1.txt','r') as f:
    data = [k.rstrip('\n') for k in f.readlines()]

cur_value = {'depth':0,'forward':0,'aim':0}

for item in data:
    item = item.split() #[[forward,down,up],[amount]]

    if item[0] == 'down':
        cur_value['aim'] += int(item[1])

    elif item[0] == 'up': 
        cur_value['aim'] -= int(item[1])

    elif item[0] == 'forward': 
        cur_value['forward'] += int(item[1])
        cur_value['depth'] += cur_value['aim'] * int(item[1])

    else: print('frik')

print(cur_value['depth'] * cur_value['forward'])