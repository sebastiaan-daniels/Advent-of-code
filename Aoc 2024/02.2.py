

class DampenerModule():
    def __init__(self, sequence:list) -> None:
        self.sequence = sequence
        if self.is_safe(self.sequence): # Original value was safe
            self.safe = True
        else:
            self.safe = self.dampener()

    def is_safe(self, line: list) -> bool:
        # is the sequence ordered?
        s1 = sorted(line)
        s2 = sorted(line)[::-1]
        if (line != s1) and (line != s2): return False # Not increasing nor decreasing
        else:
            return all([0 < abs(line[x] - line[x+1]) <= 3 for x in range(len(line)-1)])
        
    def dampener(self) -> bool:
        # brute force with every element removed once.
        removed = [self.sequence[:i] + (self.sequence[i+1::1]) for i,x in enumerate(self.sequence)]
        return any(self.is_safe(x) for x in removed)



def main():
    data = [[int(y) for y in x.strip().split()] for x in open("in02.txt", 'r').readlines()]
    
    # count safelines
    print([DampenerModule(x).safe for x in data].count(True))
    
    
if __name__ == "__main__":
    main()
