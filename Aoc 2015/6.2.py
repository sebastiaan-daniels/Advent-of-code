class gridLights():
    def __init__(self) -> None:
        # initialise the 1000x1000 grid
        self.grid = [[0 for _ in range(1000)] for _ in range(1000)] # 1kx1k grid of zero's


    def turn_range_on(self, begin: tuple, end: tuple) -> None:
        x_range = [begin[0],end[0]]
        y_range = [begin[1],end[1]]
        for x in range(x_range[0],x_range[1] + 1):
            for y in range(y_range[0],y_range[1] + 1):
                self.grid[x][y] += 1


    def turn_range_off(self, begin: tuple, end: tuple) -> None:
        x_range = [begin[0],end[0]]
        y_range = [begin[1],end[1]]
        for x in range(x_range[0],x_range[1] + 1):
                    for y in range(y_range[0],y_range[1] + 1):
                        self.grid[x][y] = self.grid[x][y] - 1 if self.grid[x][y] >= 1 else 0
    
    def toggle_range(self, begin: tuple, end: tuple) -> None:
        x_range = [begin[0],end[0]]
        y_range = [begin[1],end[1]]
        for x in range(x_range[0],x_range[1] + 1):
            for y in range(y_range[0],y_range[1] + 1):
                self.grid[x][y] += 2

    def count_on(self) -> int:
        total = 0
        for x in self.grid:
            for y in x:
                total += y

        return total


if __name__ == '__main__':
    main_grid = gridLights()
    with open('in6.txt','r') as f:
        instructions = [x.strip().split() for x in f.readlines()]

    # for each line we need to find the command
    for instr in instructions:
        if len(instr) == 4: # toggle the grid
            coords = (tuple([int(x) for x in instr[1].split(',')]),tuple([int(x) for x in instr[3].split(',')])) #extract the coordinates
            main_grid.toggle_range(coords[0],coords[1])
        elif len(instr) == 5:
            coords = (tuple([int(x) for x in instr[2].split(',')]),tuple([int(x) for x in instr[4].split(',')])) #extract the coordinates
            if instr[1] == 'off': #turn lights off
                main_grid.turn_range_off(coords[0],coords[1])
            else: # turn lights on
                main_grid.turn_range_on(coords[0],coords[1])
        else:
            raise SystemError()
        
    print(main_grid.count_on())
    #14687245
