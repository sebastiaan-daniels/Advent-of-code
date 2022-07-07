#converter from data to list
with open('in1.txt','r') as f:
    data = [int(k.rstrip('\n')) for k in f.readlines()]

#check how many are bigger
print(len([1 for index,v in enumerate(data) if index > 1 if v > data[index-1]]) + 1)
