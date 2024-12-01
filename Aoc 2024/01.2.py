def main():
    data = [x.strip() for x in open("in01.txt", 'r').readlines()]
    l1 = []
    l2 = []
    for item in data:
        data = item.split()
        l1.append(int(data[0]))
        l2.append(int(data[1]))

    sim_score = 0

    for item in l1:
        count = l2.count(item)
        sim_score += (count * item)

    print(sim_score)
    

if __name__ == "__main__":
    main()
