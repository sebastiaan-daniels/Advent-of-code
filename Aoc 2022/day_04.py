# part one
with open('input04.txt', 'r') as f:
    data = [x.split(',') for x in f.read().split('\n')[:-1]]

overlap = 0

for item in data:
    f1 = [*range(int((x := item[0].split('-'))[0]), int(x[1]) + 1)]
    f2 = [*range(int((x := item[1].split('-'))[0]), int(x[1]) + 1)]
    if all(y in f1 for y in f2) or all(x in f2 for x in f1):
        overlap += 1

print(overlap)

# part two is just changing both ALL's with ANY's