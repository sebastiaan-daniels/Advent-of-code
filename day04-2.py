#converter from data to list
with open('inday04-1.txt','r') as f:
    data = [k.rstrip('\n') for k in f.readlines()]

#class bingo???
class bingo():
    def __init__(self,card) -> None:
        self.card = card
        self.hitreg = [[False for _ in range(5)] for _ in range(5)]
    
    def __str__(self) -> str:
        return 'This is a bingo card'

    def add_hit(self,number):
        #check if number is in card
        for index1,row in enumerate(self.card):
            for index2,item in enumerate(row):
                if item == number:
                    self.hitreg[index1][index2] = True
                    return True
        return False
 
    def check_win(self):
        #check horizontal wins
        for horizontal in self.hitreg:
            if False not in horizontal: return True
        #check vertical, transpose matrix first
        transposed = self.transpose(self.hitreg)
        for horizontal in transposed:
            if False not in horizontal: return True
        return False

    def transpose(self,data):
        new = []
        for index in range(len(data)):
            new_row = []
            for item in data:
                new_row.append(item[index])
            new.append(new_row)
        return new

    def on_win(self):
        sum = 0
        for index,row in enumerate(self.hitreg):
            for index2, item in enumerate(row):
                if item == False: sum += self.card[index][index2]
        return sum

#step one, get the bingo numbers
bingo_numbers = [int(_) for _ in data[0].split(',')]

#step 2, get each bingo card

cards = []
cur_card = []
for index,line in enumerate(data):
    if index in (0,1):continue
    if line == '':
        cards.append(cur_card)
        cur_card = []
        continue
    else:
        cur_card.append([int(_) for _ in line.split()])
cards.append(cur_card)

#step 3, make each bingo card an object and make a list of all cards
data = [bingo(card) for card in cards]

#step 4, loop through each item and find the last card
last_win = None
for number in bingo_numbers:
    to_remove = []
    if len(data) == 0: break
    for card in data:
        card.add_hit(number)
        win = card.check_win()
        if win:
            last_win = [card,number]
            to_remove.append(card)
    for card in to_remove:
        data.remove(card)

print(last_win[0].on_win())


#get properties of last card
last = last_win[0]
print(last.card,last.hitreg,sep='\n')
sum_of_not = last.on_win()
    
print(f'The sum is {sum_of_not}, the current number is {last_win[1]} and the total is:\n{sum_of_not * last_win[1]}')