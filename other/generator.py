# Generates files
for day in range(1,25):
    day1 = f"{day}.1.py" if len(str(day)) > 1 else f"0{day}.1.py"
    day2 = f"{day}.2.py" if len(str(day)) > 1 else f"0{day}.2.py"
    with open(day1, 'x') as f:
        ...
    with open(day2, 'x') as f:
        ...

    
