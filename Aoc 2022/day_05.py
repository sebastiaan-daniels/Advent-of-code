# part one
with open('input05.txt', 'r') as f:
    data = [x.split(',') for x in f.read().split('\n')[:-1]]

crates = {'1':[], '2':[], '3':[], '4':[], '5':[], '6':[], '7':[], '8':[], '9':[]}
for index, item in enumerate(data):
    if index > 7: break
    for index2, item2 in enumerate(item[0]):
        if item2 in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            crates[str(((index2 + 3) // 4))].insert(0, item2)

for index, command in enumerate(data):
    if index < 10: continue
    command = [x for x in command[0] if x in '1234567890']
    if len(command) > 3:
        command[0] += command.pop(1)
    for _ in range(int(command[0])):
        crate_to_move = crates[command[1]].pop(-1)
        crates[command[2]].append(crate_to_move)

print(crates)

# part two
with open('input05.txt', 'r') as f:
    data = [x.split(',') for x in f.read().split('\n')[:-1]]

crates = {'1':[], '2':[], '3':[], '4':[], '5':[], '6':[], '7':[], '8':[], '9':[]}
for index, item in enumerate(data):
    if index > 7: break
    for index2, item2 in enumerate(item[0]):
        if item2 in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            crates[str(((index2 + 3) // 4))].insert(0, item2)

for index, command in enumerate(data):
    if index < 10: continue
    command = [x for x in command[0] if x in '1234567890']
    if len(command) > 3:
        command[0] += command.pop(1)
    for i in range(int(command[0]),0,-1):
        crate_to_move = crates[command[1]].pop(-i)
        crates[command[2]].append(crate_to_move)

print(crates)