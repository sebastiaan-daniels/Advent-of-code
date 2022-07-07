#converter from data to list
with open('in7.txt','r') as f:
    data = f.read()
    data = [int(_) for _ in data.split(',')]

no_dupl_data = list(dict.fromkeys(data))
lowest_fuel = 1E99

for hor_pos in no_dupl_data:
    total = 0
    for item in data:
        fuel = abs(hor_pos - item)
        total += fuel
    if total < lowest_fuel: lowest_fuel = total

print(lowest_fuel)