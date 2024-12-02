def is_safe(sequence:list) -> bool:
    # is the sequence ordered?
    s1 = sorted(sequence)
    s2 = sorted(sequence)[::-1]
    if (sequence != s1) and (sequence != s2): return False # Not increasing nor decreasing
    else:
        return all([0 < abs(sequence[x] - sequence[x+1]) <= 3 for x in range(len(sequence)-1)])

def main():
    data = [[int(y) for y in x.strip().split()] for x in open("in02.txt", 'r').readlines()]
    print([is_safe(x) for x in data].count(True))
    #for line in data:print(is_safe(line))

if __name__ == "__main__":
    main()
