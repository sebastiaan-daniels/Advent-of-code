def main():
    data = [x.strip() for x in open("in01.txt", 'r').readlines()]
    l1 = []
    l2 = []
    for item in data:
        data = item.split()
        l1.append(int(data[0]))
        l2.append(int(data[1]))

    l1 = sorted(l1)
    l2 = sorted(l2)
    
    diff = 0

    for index, item in enumerate(l1):
        item2 = l2[index]
        cur_diff = abs(item2-item)
        diff += cur_diff

    print(diff)

    

if __name__ == "__main__":
    main()
