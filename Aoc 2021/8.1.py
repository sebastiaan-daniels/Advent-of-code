#I have actually no clue how to do this...... updoot: way to long explanation for what we actually had to do :kek:
#get all the lines after the | in the input
with open('in8.txt','r') as f:
    data = [[x.split(' ') for x in _.rstrip('\n').split(' | ')] for _ in f.readlines()]

#we only want part 2 after |
p2 = []
for entry in data:
    p2.extend(entry[1])

#check for the amount of values that are 2,4,3,7
total = 0
for item in p2:
    if len(item) in (2,4,3,7): total += 1

print(f'The total number of displays that are 1,4,7 or 8 is: {total}')