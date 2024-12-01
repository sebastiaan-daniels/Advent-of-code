class Number():
    def __init__(self, pos_y, pos_x, value):
        self.pos_y = pos_y
        self.pos_x = pos_x
        self.value = value

    def __str__(self):
        return f"x:{self.pos_x},y:{self.pos_y},val:{self.value}"


class Grid():
    def __init__(self, non_padded_grid:list) -> None:
        self.grid = non_padded_grid
        self.padded_grid = self.pad(self.grid)
        self.numbers = self.scan()


    def pad(self, grid:list):
        grid = ["." + x + "." for x in grid]
        grid.append("."*len(grid[-1]))
        grid.insert(0, "."*len(grid[-1]))
        return grid
    
    def get_Coordinate(self, x, y) -> str:
        return self.padded_grid[y][x]
    
    def scan(self) -> list:
        scanned_nums = []
        for y, line in enumerate(self.padded_grid):
            prevnum = False
            start_x = 0
            value = ""
            for x, char in enumerate(line):
                if char in "0123456789":
                    if prevnum:
                        value += char
                    else:
                        start_x = x
                        prevnum = True
                        value += char
                else:
                    if prevnum:
                        prevnum = False
                        scanned_nums.append(Number(y, start_x, int(value)))
                        value = ""
                        start_x = 0

        return scanned_nums
    
    def __str__(self):
        return str(self.padded_grid)
        
def is_part (number: Number, grid: Grid)-> bool:
    surrounding = []
    # left
    surrounding.extend([grid.get_Coordinate(number.pos_x-1,y) for y in range(number.pos_y-1,number.pos_y+2)])
    # right
    surrounding.extend([grid.get_Coordinate(number.pos_x+len(str(number.value)),y) for y in range(number.pos_y-1,number.pos_y+2)])
    # up
    surrounding.extend([grid.get_Coordinate(x, number.pos_y-1) for x in range(number.pos_x,number.pos_x+len(str(number.value)))])
    # down
    surrounding.extend([grid.get_Coordinate(x, number.pos_y+1) for x in range(number.pos_x,number.pos_x+len(str(number.value)))])
    return any([True if x not in ".0123456789" else False for x in surrounding])
    

def main():
    total = 0
    grid = Grid([x.strip() for x in open("in03.txt", 'r').readlines()])
    for num in grid.numbers:
        if is_part(num, grid):
            total += num.value

    print(total)
 

if __name__ == "__main__":
    main()
