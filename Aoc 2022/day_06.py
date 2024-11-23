# part one
with open('input06.txt', 'r') as f:
    data = [x.split(',') for x in f.read().split('\n')[:-1]][0][0]

buffer = []
for index, item in enumerate(data):
    if len(buffer) < 4:
        buffer.append(item)
    else:
        buffer.pop(0)
        buffer.append(item)
        if len(set(buffer)) == 4:
            print(index + 1)
            break

# part two
with open('input06.txt', 'r') as f:
    data = [x.split(',') for x in f.read().split('\n')[:-1]][0][0]

buffer = []
for index, item in enumerate(data):
    if len(buffer) < 14:
        buffer.append(item)
    else:
        buffer.pop(0)
        buffer.append(item)
        if len(set(buffer)) == 14:
            print(index + 1)
            break
