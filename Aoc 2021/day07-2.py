#converter from data to list
with open('inday07-1.txt','r') as f:
    data = [int(_) for _ in f.read().split(',')]

no_dupl_data = list(dict.fromkeys(data))
lowest_fuel = 1E99

for hor_pos in no_dupl_data:
    total = 0
    for item in data:
        fuel = sum([_ for _ in range(1,abs(hor_pos-item) + 1)])
        total += fuel
    if total < lowest_fuel: lowest_fuel = total

print(lowest_fuel)