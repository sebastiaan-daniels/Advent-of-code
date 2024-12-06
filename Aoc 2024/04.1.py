from grid import Grid

class XGrid(Grid):
    ...

def main():
    data = [x.strip() for x in open("in04.txt", 'r').readlines()]
    grid = XGrid(data, 3) #max search depth beyond XMAS = 3
    words = []
    for item in grid:
        for i in range(1,9):
            words.append(grid.search(item.coordinates, 3, i))

    print(words.count("XMAS"))

    

if __name__ == "__main__":
    main()
