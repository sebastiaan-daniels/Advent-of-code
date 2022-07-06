#converter from data to list
with open('inday01-1.txt','r') as f:
    data = [int(k.rstrip('\n')) for k in f.readlines()]

list_with_sums = []
for index,item in enumerate(data):
    try:
        list_with_sums.append(item + data[index+1] + data[index+2])
    except IndexError: break

bigger = len([1 for index,v in enumerate(list_with_sums) if index > 1 if v > list_with_sums[index-1]]) + 1
print(bigger)
