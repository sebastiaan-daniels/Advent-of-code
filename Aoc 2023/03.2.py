class Number():
    def __init__(self, pos_y, pos_x, value):
        self.pos_y = pos_y
        self.pos_x = pos_x
        self.value = value
        self.gear = None
        self.already_scanned = False

    def __str__(self):
        return f"x:{self.pos_x},y:{self.pos_y},val:{self.value}"
    
    def __eq__(self, value):
        return ((self.pos_x == value.pos_x) and (self.pos_y == value.pos_y)) and (self.value == value.value)
    

class Gear():
    def __init__(self,pos_y, pos_x):
        self.pos_x = pos_x
        self.pos_y = pos_y

    def __eq__(self, value):
        return ((self.pos_x == value.pos_x) and (self.pos_y == value.pos_y))


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
        
def get_gear (number: Number, grid: Grid)-> bool:
    surrounding = []
    coordinates = []
    # left
    surrounding.extend([grid.get_Coordinate(number.pos_x-1,y) for y in range(number.pos_y-1,number.pos_y+2)])
    coordinates.extend([(number.pos_x-1,y) for y in range(number.pos_y-1,number.pos_y+2)])
    # right
    surrounding.extend([grid.get_Coordinate(number.pos_x+len(str(number.value)),y) for y in range(number.pos_y-1,number.pos_y+2)])
    coordinates.extend([(number.pos_x+len(str(number.value)),y) for y in range(number.pos_y-1,number.pos_y+2)])
    # up
    surrounding.extend([grid.get_Coordinate(x, number.pos_y-1) for x in range(number.pos_x,number.pos_x+len(str(number.value)))])
    coordinates.extend([(x, number.pos_y-1) for x in range(number.pos_x,number.pos_x+len(str(number.value)))])
    # down
    surrounding.extend([grid.get_Coordinate(x, number.pos_y+1) for x in range(number.pos_x,number.pos_x+len(str(number.value)))])
    coordinates.extend([(x, number.pos_y+1) for x in range(number.pos_x,number.pos_x+len(str(number.value)))])

    val = [True if x == "*" else False for x in surrounding]
    if any(val):
        coords = coordinates[surrounding.index('*')]
        return Gear(coords[1], coords[0])
    

def main():
    total = 0
    scanned_items = []
    grid = Grid([x.strip() for x in open("in03.txt", 'r').readlines()])
    gears_nums = []
    for number in grid.numbers:
        if gear := get_gear(number, grid):
            gears_nums.append((number, gear,))

    for item in gears_nums:
        ...
        for iter in gears_nums:
            if item[0] == iter[0]:
                # These are the same numbers!
                continue
            if item[1] == iter[1]:
                print(f"MATCH FOUND: {item} - {iter}")
                if (item[0] in scanned_items) or (iter[0] in scanned_items):
                    print("Already scanned!")
                    continue
                scanned_items.append(item[0])
                scanned_items.append(iter[0])
                ratio = item[0].value * iter[0].value
                print(ratio)
                total += ratio

            else:
                # These items don't match, continue (this is redundant code to visualise)
                continue

    print(total)
    
 

if __name__ == "__main__":
    main()
