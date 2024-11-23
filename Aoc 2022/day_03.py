# part one
with open("input03.txt",'r') as f:
    data = f.read().split('\n')[:-1]

priority = 0
ASCII_lower = 96
ASCII_upper = 38

for items in data:
    p1 = items[:len(items) // 2]
    p2 = items[len(items) // 2:]
    p1, p2 = set(p1), list(set(p2))
    double = list(p1.intersection(p2))
    if 97 <= ord(double[0]) <= 122: #  lowercase
        priority += ord(double[0]) - ASCII_lower
    else:
        priority += ord(double[0]) - ASCII_upper

print(priority)

# part two
priority = 0
ASCII_lower = 96
ASCII_upper = 38

with open("input03.txt",'r') as f:
    data = f.read().split('\n')[:-1]

# plit into parts of three
k, m = divmod(len(data), len(data) // 3)
split_parts = [data[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(len(data) // 3)]

for item in split_parts:
    assert len(item) == 3
    p1, p2, p3 = set(item[0]), set(item[1]), set(item[2])
    i1 = p1.intersection(list(p2))
    i2 = list(i1.intersection(list(p3)))

    if 97 <= ord(i2[0]) <= 122: #  lowercase
        priority += ord(i2[0]) - ASCII_lower
    else:
        priority += ord(i2[0]) - ASCII_upper

print(priority)