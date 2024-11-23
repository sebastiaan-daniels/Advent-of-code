# part one
print(max([sum([int(y) for y in x.split('\n')]) for x in open('input01.txt','r').read().split('\n\n')[:-1]]))

# part two
print(sum(sorted([sum([int(y) for y in x.split('\n')]) for x in open('input01.txt','r').read().split('\n\n')[:-1]])[-3:]))