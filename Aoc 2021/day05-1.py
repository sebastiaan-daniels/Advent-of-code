### certain code is redundant in part one, f.ex. the grid, add_to_grid() and draw_grid() are not utilised 


def main():
    #reading shit (Longest line of code! 198 characters!)
    with open('inday05-1.txt','r') as f: coords = [tuple([tuple([int(index) for index in index]) for index in [a.split(',') for a in line.split(' -> ')]]) for line in [k.rstrip('\n') for k in f.readlines()]]
    print('opened')
    #get the largest value of the grid
    max_grid = max(max(max(coords)))
    grid = [[None for _ in range(max_grid+1)] for _ in range(max_grid+1)] #+1 is because we are also counting (0,0)
    #draw_grid(grid)

    #for part one, convert coordinates to list with only vertical or horizontal lines
    coords_hor_ver = [coord for coord in coords if coord[0][0] == coord[1][0] or coord[0][1] == coord[1][1]] 
    print('hor/ver found')
    #find all the coordinates that are included in the lines
    all_coords = []
    for coord in coords_hor_ver:
        line = find_connection(coord)
        all_coords.extend(line)

    #for now, we don't actually need to append coordinates to the grid, we just figure out how many duplicate coordinates we have
    print('finding doubles')
    doubles = list_duplicates(all_coords)
    print(f'The amount of overlapping lines is {len(doubles)}')

def find_connection(coord:tuple) -> list: #finds all the coordinates in a line ((x1,y1),(x2,y2))
    #horizontal cases (y1 = y2)
    if coord[0][1] == coord[1][1]:
        step= 1
        if coord[1][0] < coord [0][0]: step = -1
        if step == 1:
            new = [(_,coord[0][1]) for _ in range(coord[0][0],coord[1][0] + 1,step)]
        else:
            new = [(_,coord[0][1]) for _ in range(coord[0][0],coord[1][0] - 1,step)]
        return new
    #vertical cases (x1 = x2)
    if coord[0][0] == coord[1][0]:
        step = 1
        if coord[1][1] < coord [0][1]: step = -1
        if step == 1:
            new = [(coord[0][0],_) for _ in range(coord[0][1],coord[1][1] + 1,step)]
        else: 
            new = [(coord[0][0],_) for _ in range(coord[0][1],coord[1][1] - 1,step)]
        return new

def add_to_grid(coord):
    pass

def list_duplicates(seq):
    seen = set()
    seen_add = seen.add
    # adds all elements it doesn't know yet to seen and all other to seen_twice
    seen_twice = set( x for x in seq if x in seen or seen_add(x) )
    # turn the set into a list (as requested)
    return list( seen_twice )

def draw_grid(grid):
    for line in grid:
        for item in line: 
            if item == None: item = '.'
            print(f'{item}',end='')
        print('')

if __name__ == "__main__":
    main()
