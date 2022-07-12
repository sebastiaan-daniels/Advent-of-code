class coords():
    def __init__(self) -> None:
        self.coords = [0,0]
        self.cur_orientation = 'up'

    def up(self, x):
        self.coords[1] += x

    def down(self, x):
        self.coords[1] -= x

    def left(self, x):
        self.coords[0] -= x

    def right(self, x):
        self.coords[0] += x

    def make_move(self, M, amount):
        print(self.cur_orientation,M,amount)
        if self.cur_orientation == 'up':
            if M == 'L':
                self.cur_orientation = 'left'
                self.left(amount)
            elif M == 'R':
                self.cur_orientation = 'right'
                self.right(amount)
            else: raise ValueError()
        elif self.cur_orientation == 'down':
            if M == 'L':
                self.cur_orientation = 'right'
                self.right(amount)
            elif M == 'R':
                self.cur_orientation = 'left'
                self.left(amount)
            else: raise ValueError()
        elif self.cur_orientation == 'left':
            if M == 'L':
                self.cur_orientation = 'down'
                self.down(amount)
            elif M == 'R':
                self.cur_orientation = 'up'
                self.up(amount)
            else: raise ValueError()
        elif self.cur_orientation == 'right':
            if M == 'L':
                self.cur_orientation = 'up'
                self.up(amount)
            elif M == 'R':
                self.cur_orientation = 'down'
                self.down(amount)
            else: raise ValueError()
        print(self.cur_orientation, self.coords)


with open('in1.txt','r') as f:
    instr =  [(x[0],int(x[1])) for x in f.read().split()]
    #instr = [(x[0],int(x[1])) for x in "R5, L5, R5, R3".split()]

coordinates = coords()
print(coordinates.coords, coordinates.cur_orientation)
for move in instr:
    print(move)
    coordinates.make_move(move[0],move[1])
print(coordinates.coords)