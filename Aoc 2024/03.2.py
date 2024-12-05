import re
def main():
    data =open("in03.txt", 'r').read()

    r = re.findall(r"(mul\(\d+,\d+\)){1}|(do\(\)){1}|(don't\(\)){1}", data)
    filtered = [x[0] if x[0] != "" else x[1] if x[1] != "" else x[2] for x in r]
    calc = True
    total = 0
    for instruction in filtered:
        if instruction == "do()":
            calc = True
        elif instruction == "don't()":
            calc = False
        else:
            if calc:
                total += get_mult(instruction)

    print(total)


    
    print(total)

def get_mult(mult:str) -> int:
    return (lambda a,b: int(a)*int(b))( *mult[4:-1].split(','))
    

if __name__ == "__main__":
    main()


#
