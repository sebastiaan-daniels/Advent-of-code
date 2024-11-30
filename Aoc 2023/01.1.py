
print(sum([(lambda x: int(f'{x[0]}{x[-1]}'))([x for x in line if x in '0123456789']) for line in [x.strip() for x in open("in01.txt", 'r').readlines()]]))

    