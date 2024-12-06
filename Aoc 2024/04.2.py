from grid import Grid

class XGrid(Grid):
    ...

def main():
    data = [x.strip() for x in open("in04.txt", 'r').readlines()]
    grid = XGrid(data, 3) #max search depth beyond XMAS = 3
    total = 0
    for item in grid:
        if item.item == "A":
            # For X-mas, indexes 0,2,5,7 are important
            n = grid.neighbours(item.coordinates)
            neighbours = n[0] + n[2] + n[5] + n[7]
            if neighbours in ["SSMM", "MMSS", "MSMS", "SMSM"]:
                total += 1

    print(total)


    

if __name__ == "__main__":
    main()
