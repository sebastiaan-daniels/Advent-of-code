"""
Advent of code is known for it's extended usage of grids...
So to spare me some time in the future this class will be helpfull.
It also helps with padding and padded grids.

"""

class GridItem():
    """
    Class used to represent a single item in a Grid.
    Gives more information about an item.
    """
    def __init__(self, item_value, x, y):
        self.item = item_value
        self.coordinates = (x,y,)
        # redundancy
        self.x = x
        self.y = y

    def __str__(self):
        return f"item: {self.item}, x: {self.x}, y: {self.y}"



class Grid():
    def __init__(self, grid: list[list], padding: int = 0) -> None:
        self.grid = grid
        self.padding = padding
        if padding > 0 :
            self.padded_grid = self.pad(self.grid, padding)
        else:
            self.padded_grid = self.grid

    def pad(self, grid: list[list], amount: int) -> list[list]:
        """
        Pads the grid with the specified amount
        """
        grid = ["."*amount + x + "."*amount for x in grid]
        for _ in range(amount):
            grid.append("."*len(grid[-1]))
            grid.insert(0, "."*len(grid[-1]))
        return grid
    
    def getCoordinate(self, x: int, y: int) -> str:
        return self.grid[y][x]
    
    def getPaddedCoordinate(self, x: int, y: int) -> str:
        """
        This function is very useful for getting a coordinate from a padded grid. F.ex in this grid:
        .......
        .......
        ..123..
        ..456..
        .......
        .......

        asking for (0,0) would return 1
        asking for (2,1) would return 6
        asking for (1,1) would return 5
        """
        return self.padded_grid[y+self.padding][x+self.padding]
    
    def getSize(self) -> set[int,int]:
        """
        Returns the (x,y) size of the grid
        abdgfs
        fhfsja

        => (6,2)
        """
        y_size = len(self.grid)
        x_size = len(self.grid[0])
        return (x_size, y_size,)
    

    def search(self, coordinate: set[int,int], distance: int, direction: int) -> str:
        """
        This is a very fun function to search what follows a certain coordinate in ANY direction for a set length.
        Users are responsible to enter and verify where they search as an error for searching outside the grid isn't filtered.
        This function uses the padded grid and coordinates.

        123
        4.5
        678

        => Search Directions 
        """
        # Define direction deltas for movement (dx, dy)
        directions = {
            1: (-1, -1),  # Up-Left
            2: (0, -1),   # Up
            3: (1, -1),   # Up-Right
            4: (-1, 0),   # Left
            5: (1, 0),    # Right
            6: (-1, 1),   # Down-Left
            7: (0, 1),    # Down
            8: (1, 1)     # Down-Right
        }
        
        if direction not in directions:
            raise ValueError(f"Invalid direction {direction}. Must be between 1 and 8.")
        
        dx, dy = directions[direction]
        x, y = coordinate
        result = [self.getPaddedCoordinate(x,y),]
        
        for _ in range(distance):
            x += dx
            y += dy
            result.append(self.getPaddedCoordinate(x, y))  # Safely access padded grid
        
        return ''.join(result)
    
    def neighbours(self, coordinate: tuple[int, int]) -> list[str]:
        """
        Returns a list of the neighbors of a coordinate in a padded grid:
        Neighbors are indexed as follows:
        012
        3X4
        567
        """
        x, y = coordinate
        deltas = [
            (-1, -1), (0, -1), (1, -1),  # Top-left, Top, Top-right
            (-1, 0),          (1, 0),   # Left,      Right
            (-1, 1), (0, 1), (1, 1)     # Bottom-left, Bottom, Bottom-right
        ]
        neighbors = []
        for dx, dy in deltas:
            nx, ny = x + dx, y + dy
            neighbors.append(self.getPaddedCoordinate(nx, ny))
        return neighbors

    def __str__(self):
        return str(self.padded_grid)
    
    def __sizeof__(self):
        # Same as the size function
        return self.getSize()
    
    def __iter__(self):
        """
        Allows iteration over the grid items.
        """
        for y, row in enumerate(self.grid):
            for x, item in enumerate(row):
                yield GridItem(item, x, y)
    

# Tests
if __name__ == "__main__":
    grid = Grid(["".join([str(_) for _ in range(5)]) for _ in range(5)], 2)
    print(grid)
    for item in grid:
        print(item)