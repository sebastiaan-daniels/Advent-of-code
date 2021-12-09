#converter from data to list
with open('inday06-1.txt','r') as f:
    data = f.read()
    data = [int(_) for _ in data.split(',')]

#make dict and append gen 1 to it
old = {k:0 for k in range(9)}
for item in data:
    old[item] += 1
print(old)

def next_gen(old):
    new = {k:0 for k in range(9)}
    #easy cases
    #0,1,2,3,4,5,7
    new[0] = old[1]
    new[1] = old[2]
    new[2] = old[3]
    new[3] = old[4]
    new[4] = old[5]
    new[5] = old[6]
    new[7] = old[8]
    #special cases 6,8
    new[8] = old[0]
    new[6] = old[0]
    new[6] += old[7]
    return new

for a in range(256): #range is the # of days
    old = next_gen(old)

print(sum([v for (k,v) in old.items()]))

##### literally the same as 06-1 but with line 29 changed (range(80) -> range(256))