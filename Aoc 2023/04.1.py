class Card():
    def __init__(self, line:str) -> None:
        split1 = line.split(':')
        self.id = int(split1[0][5:].strip())
        split2 = split1[1].split('|')
        self.winning_nums = [int(x) for x in split2[0].split()]
        self.nums = [int(x) for x in split2[1].split()]

    def found_nums(self) -> list:
        num_list = []
        for item in self.winning_nums:
            if item in self.nums:
                num_list.append(item)
        return num_list
    
    def score(self) -> int:
        found = self.found_nums()
        if len(found) == 0:
            return 0
        else:
            return 2**(len(found)-1)

def main():
    score = 0
    cards = []
    data = [x.strip() for x in open("in04.txt", 'r').readlines()]
    cards.extend([Card(x) for x in data])
    
    for card in cards:
        score += card.score()

    print(score)
    

if __name__ == "__main__":
    main()
